#![allow(unused, non_snake_case)]

#[macro_use]
extern crate lazy_static;

use hashbrown::HashMap;
use itertools::Combinations;
use pyo3::{prelude::*, types::PyType};
use rayon::prelude::*;
use regex::Regex;
use serde::{Deserialize, Serialize};
use serde_json::from_str;
use std::borrow::Borrow;
use std::fs::read_to_string;
use std::num;
use std::{path::PathBuf, thread, vec};

macro_rules! hashmap {
        ($( $key: expr => $val: expr ),*) => {{
        let mut map = ::hashbrown::HashMap::new();
        $( map.insert($key, $val); )*
        map
    }}
}

#[derive(Serialize, Deserialize, Clone, Debug)]
struct GeneTable {
    table_id: String,
    A: Option<Vec<String>>,
    L: Option<Vec<String>>,
    W: Option<Vec<String>>,
    Q: Option<Vec<String>>,
    Y: Option<Vec<String>>,
    E: Option<Vec<String>>,
    C: Option<Vec<String>>,
    D: Option<Vec<String>>,
    F: Option<Vec<String>>,
    G: Option<Vec<String>>,
    H: Option<Vec<String>>,
    I: Option<Vec<String>>,
    M: Option<Vec<String>>,
    K: Option<Vec<String>>,
    P: Option<Vec<String>>,
    R: Option<Vec<String>>,
    S: Option<Vec<String>>,
    V: Option<Vec<String>>,
    N: Option<Vec<String>>,
    T: Option<Vec<String>>,
    STOP: Option<Vec<String>>,
    DASH: Option<Vec<String>>,
}

impl GeneTable {
    pub fn from(filepath: PathBuf, table_id: u8) -> Self {
        let str_read = read_to_string(filepath).expect("Error reading file");

        let gene_tables: Vec<GeneTable> = from_str(&str_read).unwrap();

        let mut gene_table = gene_tables
            .iter()
            .cloned()
            .filter(|x| x.table_id == table_id.to_string())
            .collect::<Vec<GeneTable>>()
            .get(0)
            .unwrap()
            .clone();

        gene_table.set_dash();

        gene_table
    }

    pub fn set_dash(&mut self) {
        self.DASH = Some(vec!["".to_string()]);
    }

    pub fn get_by_char(&self, c: &char) -> &Option<Vec<String>> {
        match c {
            'A' => &self.A,
            'L' => &self.L,
            'W' => &self.W,
            'Q' => &self.Q,
            'Y' => &self.Y,
            'E' => &self.E,
            'C' => &self.C,
            'D' => &self.D,
            'F' => &self.F,
            'G' => &self.G,
            'H' => &self.H,
            'I' => &self.I,
            'M' => &self.M,
            'K' => &self.K,
            'P' => &self.P,
            'R' => &self.R,
            'S' => &self.S,
            'V' => &self.V,
            'N' => &self.N,
            'T' => &self.T,
            '*' => &self.STOP,
            '-' => &self.DASH,
            _ => panic!("No acceptable index for gene table, must be one of the 18 AA chars + 4 ambiguous chars.")
        }
    }

    pub fn get_by_amb_char(&self, amb_char: AmbiguousChars) -> Vec<Option<Vec<String>>> {
        match amb_char {
            AmbiguousChars::X | AmbiguousChars::Period => vec![Some(vec!["...".to_string()])],
            AmbiguousChars::B => vec![self.D.clone(), self.N.clone()],
            AmbiguousChars::Z => vec![self.E.clone(), self.Q.clone()],
            AmbiguousChars::J => vec![self.I.clone(), self.L.clone()],
        }
    }

    pub fn map_singe_aa_seq_to_triplets(
        &self,
        amino_acid: &String,
    ) -> Vec<Vec<String>> {
        let mut ret_vec = vec![];


        amino_acid.chars().for_each(|c| {
            match AmbiguousChars::matches_ambiguous(&c) {
                true => {
                    let amb_char = AmbiguousChars::from(c);
                    let mut v_final = vec![];

                    let vec_opt_vec_triplets = self.get_by_amb_char(amb_char);

                    vec_opt_vec_triplets.iter().cloned().for_each(|x| match x {
                        Some(v) => v_final.extend(v),
                        None => (),
                    });

                    ret_vec.push(v_final);
                }
                false => match &self[c] {
                    Some(v) => {
                        ret_vec.push(v.clone());
                    }
                    None => (),
                },
            }
        });

        ret_vec
    }
}

impl std::ops::Index<char> for GeneTable {
    type Output = Option<Vec<String>>;

    fn index(&self, index: char) -> &Self::Output {
        self.get_by_char(&index)
    }
}

enum AmbiguousChars {
    X,
    Period,
    B,
    Z,
    J,
}

impl AmbiguousChars {
    pub fn from(c: char) -> Self {
        match c {
            'X' => Self::X,
            '.' => Self::Period,
            'B' => Self::B,
            'Z' => Self::Z,
            'J' => Self::J,
            _ => panic!("The character must be [X*.BZJ]"),
        }
    }

    pub fn matches_ambiguous(c: &char) -> bool {
        vec!['X', '.', 'B', 'Z', 'J'].contains(c)
    }
}

struct AminoAcidTranslator(String);

impl AminoAcidTranslator {
    pub fn streamline_amino_acid(&mut self) {
        let AminoAcidTranslator(amino_acid) = self;

        let mut amino_acid_trimmed = amino_acid.trim().to_uppercase();

        let mut amino_acid_filtered = String::new();

        amino_acid_trimmed
            .chars()
            .for_each(|c| {
                match vec![
                    'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
                    'T', 'V', 'W', 'Y', 'X', 'B', 'Z', 'J', '*', '-',
                ].contains(&c) && !c.is_numeric() {
                    true => {
                        amino_acid_filtered.push(c)
                    },
                    false => (),
                } 
        });

        *amino_acid = amino_acid_filtered;

    }

    pub fn reverse_translate_and_compare(
        &self,
        compare_dna: &String,
        gene_table: &GeneTable,
    ) -> String {
        let AminoAcidTranslator(amino_acid) = self;

        let range_map = gene_table.map_singe_aa_seq_to_triplets(amino_acid);
        let mut final_str = String::new();
        
        let mut i = 0;

        range_map
            .into_iter()
            .zip(amino_acid.chars())
            .for_each(|(possible_triplets, compare_substr_aa)| {
               
                match compare_substr_aa == '-' {
                    true => {
                        final_str.push_str("---");
                    },
                    false => {
                        let compare_substr_nuc = compare_dna[i..=i + 2].to_string();

                        i += 3;

                        possible_triplets
                            .iter()
                            .cloned()
                            .for_each(|s| {

                                match s == compare_substr_nuc {
                                    true => {
                                        final_str.push_str(&s)
                                    },
                                    false => (),
                                };
                            } )
                    }
                }
               
            });

        final_str
    }
}

#[pyfunction]
fn pn2codon(
    filepath: PathBuf,
    table_id: u8,
    amino_seqs: Vec<(String, String)>,
    nuc_seqs: Vec<(String, String)>,
) -> Vec<(String, String)> {
    let gene_table = GeneTable::from(filepath, table_id);

    amino_seqs
        .par_iter()
        .zip(nuc_seqs.par_iter())
        .map(|((aa_id, aa), (nn_id, nn))| {
            if aa_id != nn_id {
                panic!("Nuc seqs and AA seqs must be in the same order of (id, aa), (id, nn)");
            }

            let mut amino_acid = AminoAcidTranslator(aa.clone());
            amino_acid.streamline_amino_acid();

            let codon = amino_acid.reverse_translate_and_compare(nn, &gene_table);

            (nn_id.clone(), codon)
        })
        .collect()
}

/// A Python module implemented in Rust.
#[pymodule]
fn pro2codon(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(pn2codon, m)?)?;
    Ok(())
}


#[test]
fn test_revtrans() {
    let nuc = vec![("aa".to_string(), String::from("ATGTGCCATCAGCATCCGAATCATTTGCTGAAGCAGTCTCTCCAAACGTACGTGTTCCGCCGAAATGAGCTACTGGACGCCGGCAAAAGTGCACTGCGGCATCGCATTCGCCTTCAGGAGCGAAATTGGATGACGACAGGGGCCAAACCACAGCAGCAGCAAGTCGTGCGAACCGGGGAAAGGAGCTCAAGGGTTCTGAGGTTACTGCTGGCAGGAACCGCCGTGAGTGTCACCGTAGGGTATCAATGCCGCCGGTGGTTCGTGCATTGTGAAGCGGCTGTTGTAAACAACCGGCTGGTGGGACAGAAGGTTCCGGGAGCAGGAGATGGGATCAAATTTGACTGGAGGAAATTTTGGAGCTATTTGAGACCGCACCTGGTGAAACTGATTGGGGCGATTATGGCGGCGCTGGCCGTGGCCTATTTTAATATTCAGATTCCCAACATGCTGGGAGTAGTGGTGAATACGCTGTCGAAATATGCCAGGACGAGTTTGAGCGACATTGATTCTTCAACGTTCATGAACGAAATGAAACTGCCATCGCTGCGACTGTTCGGTATGTACATTGCCCAAGCCGGATTCACATTCGTCTACATTTTGCTGCTGAGTCAGATAGGCGAACAGATGGCCGCGAAGATCCGACAGGATCTGTTCAAGCAGATCATCATCCAGGATCTGGAGTTCTTCGACGAAAACCGAACCGGAGAGTTGGTCAACCGGTTGACGGCCGACGTGCAAGACTTCAAATCTAGCTTCAAGCAATGCATCTCGCAAGGATTACGGTCATTTGCCCAGCTGATCGGAGGTGGCATATCGTTGTTCCTTATCTCGCCACAGCTGGCCAGTATCGCTTTGGTATCGGTCCCTGCCGCGGTGGCAATGTTCTCCTTTCTTGGAAAGTCTTTGAGAGCGCTGAGCAAGAAGAGTCAAGCCCAATCGGAACGAGCGACTTCAGTGAGTGAGGAAGCGCTGTCCAACATCAGAACTGTCCGCTCCAGTGCATGCGAGTTTGCCGAAGTTGAACTGTTGCGGCAGGAAACGGAAAAGGCAGCTGAGCTGTCCCAGCAGCTGGGTGTGAAATCGCACTCTATCATGCCACTGACTAATTTATACGTGAACGGCATGGTGCTAAACGACGCTGGTTCTCGTTCAATAAGTGCCGGAGATTTGATGGCATTCTTGGTTGCATCTCAAGGTGTTCAACGCTCTCTTGCCCAAGGCTCTATTCTGCTTGGATCCGTAATCCGTGGAATGACAGCCGGCACCCGTGTATTCGAATACCTCTCGGTTCAGCCTAAAGTAGATCTCAAATACGGACAAATCATTCCCGAGTCGGAAATTCGTGGCGAAATCCGATTCGAAAACGTGTCTTTCACGTATCCTTCCCGACCCAATCATCCTGTTCTCAAAAACTTTTCGCTTGTCCTGAAACCTGGACAAACTGTGGCCCTGGTGGGAGCCAGTGGCTCAGGGAAATCGACCATTGCTTCGCTTCTGGAGCGATTTTACGAGCCAACCGGTGGCCGCATCACCATAGATGGTTATGAACTCTCACAATTGTCGCCTTATTGGCTCCGAGGCCACCTGATAGGATTCATCGAACAGCAACCGATACTGTTCGGAACGTCCATCTACGAGAACATACGCTACGGCCGTCCAGAGGCGTCACAAGCGGAAGTCCTGGAAGCGGCCAAGCTGTCTCAGTCGCATCAGTTTGTGAGCAAATTGCCTGAGGGCTACGAGACGCCAGTTGGCGAAAGGGGCATCCAACTGAGTGGTGGCCAACGGCAAAGGATAGCAATAGCTAGAGCTTTGCTCAAACAGCCCTCGGTGTTGATCTTGGACGAGGCTACCAGTGCATTAGATGCTTCCAGTGAGGCCATCGTGCAGAAAGCCCTTGATGCAGCGGTAGTCGACAGAACTACGCTGGTTATTGCCCACCGGCTATCAACCATCAGGAACGCGGATGTGATTGTGGTGCTGGAAAAAGGCCGAATAGTAGAGATTGGCAATCATGATGCGCTGCTGCGCAAGAAGGGCTACTACTTTGAACTGGTCAAACAGCAAGAACGGGAACAACGCGAGGAACAACAGCAAAGGGCCTACGGA"))];
    let aa = vec![("aa".to_string(), String::from("MC-------HQHPNHLLKQSLQTYVFRRNELLDAGKSALR-HRIRLQERNWMTTGAKPQQQQVVRTGERSSRVLR-------LLLAGTA----VSVTVGYQCRRWF-------VHCEAAVVNNRLVG--QKVPG-AGDGIKFDWRKFWSYLRPHLVKLIGAIMAALAVAYFNIQIPNMLGVVVNTLSKYARTSLSDIDSSTFMNEMKLPSLRLFGMYIAQAGFTFVYILLLSQIGEQMAAKIRQDLFKQIIIQDLEFFDENRTGELVNRLTADVQDFKSSFKQCISQGLRSFAQLIGGGISLFLISPQLASIALVSVPAAVAMFSFLGKSLRALSKKSQAQ----------SERATSVSEEALSNIRTVRSSACEFAEVELLRQETEKAAELSQQLGVKSHSIMPLTNLYVNGMVLND-------AGSRSISAGDLMAFLVASQGVQRSLAQGSILLGSVIRGMTAGTRVFEYLSVQPKVDLKYGQIIPESEIRGEIRFENVSFTYPSRPNHPVLKNFSLVLKPGQTVALVGASGSGKSTIASLLERFYEPTGGRITIDGYELSQLSPYWLRGHLIGFIEQQPILFGTSIYENIRYGRPEASQAEVLEAAKLSQSHQFVSKLPEGYETPVGERGIQLSGGQRQRIAIARALLKQPSVLILDEATSALDASSEAIVQKALDAAVVDRTTLVIAHRLSTIRNADVIVVLEKGRIVEIGNHDALLRKKGYYFELVKQQEREQREEQQQRAYG------------"))];
    let table_id = 1u8;
    let filepath = PathBuf::from("genetic_table.json");

    let codon = pn2codon(filepath, table_id, aa, nuc);

    let should_be = String::from("ATGTGC---------------------CATCAGCATCCGAATCATTTGCTGAAGCAGTCTCTCCAAACGTACGTGTTCCGCCGAAATGAGCTACTGGACGCCGGCAAAAGTGCACTGCGG---CATCGCATTCGCCTTCAGGAGCGAAATTGGATGACGACAGGGGCCAAACCACAGCAGCAGCAAGTCGTGCGAACCGGGGAAAGGAGCTCAAGGGTTCTGAGG---------------------TTACTGCTGGCAGGAACCGCC------------GTGAGTGTCACCGTAGGGTATCAATGCCGCCGGTGGTTC---------------------GTGCATTGTGAAGCGGCTGTTGTAAACAACCGGCTGGTGGGA------CAGAAGGTTCCGGGA---GCAGGAGATGGGATCAAATTTGACTGGAGGAAATTTTGGAGCTATTTGAGACCGCACCTGGTGAAACTGATTGGGGCGATTATGGCGGCGCTGGCCGTGGCCTATTTTAATATTCAGATTCCCAACATGCTGGGAGTAGTGGTGAATACGCTGTCGAAATATGCCAGGACGAGTTTGAGCGACATTGATTCTTCAACGTTCATGAACGAAATGAAACTGCCATCGCTGCGACTGTTCGGTATGTACATTGCCCAAGCCGGATTCACATTCGTCTACATTTTGCTGCTGAGTCAGATAGGCGAACAGATGGCCGCGAAGATCCGACAGGATCTGTTCAAGCAGATCATCATCCAGGATCTGGAGTTCTTCGACGAAAACCGAACCGGAGAGTTGGTCAACCGGTTGACGGCCGACGTGCAAGACTTCAAATCTAGCTTCAAGCAATGCATCTCGCAAGGATTACGGTCATTTGCCCAGCTGATCGGAGGTGGCATATCGTTGTTCCTTATCTCGCCACAGCTGGCCAGTATCGCTTTGGTATCGGTCCCTGCCGCGGTGGCAATGTTCTCCTTTCTTGGAAAGTCTTTGAGAGCGCTGAGCAAGAAGAGTCAAGCCCAA------------------------------TCGGAACGAGCGACTTCAGTGAGTGAGGAAGCGCTGTCCAACATCAGAACTGTCCGCTCCAGTGCATGCGAGTTTGCCGAAGTTGAACTGTTGCGGCAGGAAACGGAAAAGGCAGCTGAGCTGTCCCAGCAGCTGGGTGTGAAATCGCACTCTATCATGCCACTGACTAATTTATACGTGAACGGCATGGTGCTAAACGAC---------------------GCTGGTTCTCGTTCAATAAGTGCCGGAGATTTGATGGCATTCTTGGTTGCATCTCAAGGTGTTCAACGCTCTCTTGCCCAAGGCTCTATTCTGCTTGGATCCGTAATCCGTGGAATGACAGCCGGCACCCGTGTATTCGAATACCTCTCGGTTCAGCCTAAAGTAGATCTCAAATACGGACAAATCATTCCCGAGTCGGAAATTCGTGGCGAAATCCGATTCGAAAACGTGTCTTTCACGTATCCTTCCCGACCCAATCATCCTGTTCTCAAAAACTTTTCGCTTGTCCTGAAACCTGGACAAACTGTGGCCCTGGTGGGAGCCAGTGGCTCAGGGAAATCGACCATTGCTTCGCTTCTGGAGCGATTTTACGAGCCAACCGGTGGCCGCATCACCATAGATGGTTATGAACTCTCACAATTGTCGCCTTATTGGCTCCGAGGCCACCTGATAGGATTCATCGAACAGCAACCGATACTGTTCGGAACGTCCATCTACGAGAACATACGCTACGGCCGTCCAGAGGCGTCACAAGCGGAAGTCCTGGAAGCGGCCAAGCTGTCTCAGTCGCATCAGTTTGTGAGCAAATTGCCTGAGGGCTACGAGACGCCAGTTGGCGAAAGGGGCATCCAACTGAGTGGTGGCCAACGGCAAAGGATAGCAATAGCTAGAGCTTTGCTCAAACAGCCCTCGGTGTTGATCTTGGACGAGGCTACCAGTGCATTAGATGCTTCCAGTGAGGCCATCGTGCAGAAAGCCCTTGATGCAGCGGTAGTCGACAGAACTACGCTGGTTATTGCCCACCGGCTATCAACCATCAGGAACGCGGATGTGATTGTGGTGCTGGAAAAAGGCCGAATAGTAGAGATTGGCAATCATGATGCGCTGCTGCGCAAGAAGGGCTACTACTTTGAACTGGTCAAACAGCAAGAACGGGAACAACGCGAGGAACAACAGCAAAGGGCCTACGGA------------------------------------");

    assert_eq!(codon[0].1, should_be);

}