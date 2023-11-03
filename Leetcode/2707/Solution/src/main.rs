struct Solution {}

use std::collections::{HashSet, HashMap};
use std::convert::TryInto;

impl Solution {
    fn populate_data_structures(s: &String, dictionary: Vec<String>, starting_from: &mut HashMap<usize, Vec<usize>>) {
        let n = s.len();
        let mut hashed_dict : HashSet<String> = Default::default();

        for given_string in dictionary {
            hashed_dict.insert(given_string);
        }

        for i in 0..n {
            for j in i..n {
                if hashed_dict.contains(&s[i..j+1]) {
                    let v = starting_from.get_mut(&i);
                    if v.is_none() {
                        starting_from.insert(i, Vec::from([j]));
                    } else {
                        v.unwrap().push(j);
                    }
                }
            }
        }
    }

    fn find_min_extra_from(s: &String, start: usize, starting_from: &HashMap<usize, Vec<usize>>, known_minimums: &mut HashMap<usize, usize>) {
        let n = s.len();
        if start >= n {
            known_minimums.insert(start, 0);
            return;
        }

        if known_minimums.contains_key(&start) {
            return;
        }

        let mut minimum_extra = usize::pow(10, 10);
        if starting_from.contains_key(&start) {
            let intervals = &starting_from[&start];
            for end in intervals {
                if *end == n - 1 {
                    known_minimums.insert(start, 0);
                    return;
                }
                Self::find_min_extra_from(s, end + 1, &starting_from, known_minimums);
                let candidate = known_minimums[&(*end + 1)];
                if candidate < minimum_extra {
                    minimum_extra = candidate;
                }
            }
        }

        // Case where even if there is a match, we count the character as an extra character.
        Self::find_min_extra_from(&s, start + 1, &starting_from, known_minimums);
        let candidate = 1 + known_minimums[&(start + 1)];
        if candidate < minimum_extra {
            minimum_extra = candidate;            
        }

        known_minimums.insert(start, minimum_extra);
    }

    pub fn min_extra_char(s: String, dictionary: Vec<String>) -> i32 {
        let mut starting_from : HashMap<usize, Vec<usize>> = Default::default();
        Self::populate_data_structures(&s, dictionary, &mut starting_from);
        let mut known_minimums: HashMap<usize, usize> = Default::default();
        Self::find_min_extra_from(&s, 0, &starting_from, &mut known_minimums);
        println!("starting_from = {:?}\nknown_minimums = {:?}", starting_from, known_minimums);
        known_minimums[&0].try_into().unwrap()
    }
}

use std::fs::File;
use std::io::prelude::*;
use std::path::PathBuf;

struct FileHandler {
    path : PathBuf,
}

impl FileHandler {
    fn tokenizeString(&self, s: &mut String) -> Vec<String> {
        // We expect a list of comma separated values.
        // println!("{}", s);
        s.retain(|ch| ch != '[' && ch != ']' && ch != '\"' && ch != ' ');
        println!("after retain = {:?}", s);
        let values : Vec<String> = s.split(',').map(String::from).collect();
        // println!("values = {:?}", values);
        values
    }

    pub fn readAndTokenizeInput(&self) -> Vec<Vec<String>> {
        let s : String = self.readFileContents();

        let mut result = Vec::new();
        for line in s.lines() {
            result.push(self.tokenizeString(&mut line.to_string()));
        }

        result
    }

    fn readFileContents(&self) -> String {
        let display = self.path.to_str().unwrap();

        // Open file in read-only mode.
        let mut file = match File::open(&self.path) {
            Err(why) => panic!("Couldn't open {}: {}", display, why),
            Ok(file) => file,
        };

        let mut s = String::new();
        match file.read_to_string(&mut s) {
            Err(why) => panic!("couldn't read {}: {}", display, why),
            Ok(_) => s,
        }
    }
}

fn main() {
    let mut fh = FileHandler {
        path : PathBuf::new()
    };

    let path = std::env::current_exe().unwrap();
    fh.path = path.parent().unwrap().parent().unwrap().parent().unwrap().join("src").join("2707.text");

    let all_lines = fh.readAndTokenizeInput();

    for i in 0..all_lines.len() {
        let s = &all_lines[i][0];
        let dictionary = &all_lines[i + 1];
        println!("For s = {} dictionary = {:?} answer is {}", s, dictionary, Solution::min_extra_char(s.clone(), dictionary.clone()));
    }
}
