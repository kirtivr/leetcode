struct Solution {}

use std::collections::{HashSet, HashMap};
use std::convert::TryInto;

impl Solution {
    fn do_traversal_from(start: i32, connections: &mut HashMap<i32, Vec<i32>>) -> HashSet<i32> {
        let mut stk: Vec<i32> = vec![start];
        let mut out: HashSet<i32> = Default::default();
        out.insert(start);

        while stk.len() > 0 {
            let top = stk.pop().unwrap();

            if !connections.contains_key(&top) {
                continue;
            }

            for node in &connections[&top] {
                if *node != top {
                    stk.push(*node);
                    out.insert(start);
                }  
             }
        }

        return out;
    }
    pub fn min_malware_spread(graph: &Vec<Vec<i32>>, initial: &Vec<i32>) -> i32 {
        let mut connections: HashMap<i32, Vec<i32>> = Default::default();
        for i in 0..graph.len() {
            for j in 0..graph[i].len() {
                let i_32 = i.try_into().unwrap();
                let j_32 = j.try_into().unwrap();
                if connections.contains_key(&i_32) {
                    connections.get_mut(&i_32).unwrap().push(j_32);
                } else {
                    connections.insert(i_32, vec![j_32]);
                }
            }
        }

        // Find all connected components in the graph.
        let mut connected_components: HashMap<i32, HashSet<i32>> = Default::default();
        let mut max_components = (0, -1);
        for start in initial {
            let components = Self::do_traversal_from(*start, &mut connections);
            if max_components.0 < components.len() {
                max_components = (components.len(), *start);
            }
            connected_components.insert(*start, components);
        }

        max_components.1
    }
}

use std::fs::File;
use std::io::prelude::*;
use std::path::PathBuf;

struct FileHandler {
    path : PathBuf,
}

impl FileHandler {
    fn tokenizeString(&self, s: &mut String) -> Vec<i32> {
        // We expect a list of comma separated values.
        // println!("{}", s);
        s.retain(|ch| ch != '[' && ch != ']' && ch != '\"' && ch != ' ');
        let values : Vec<i32> = s.split(',').map(|x| x.parse::<i32>().unwrap()).collect();
        // println!("values = {:?}", values);
        values
    }

    pub fn readAndTokenizeInput(&self) -> Vec<Vec<i32>> {
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
    fh.path = path.parent().unwrap().parent().unwrap().parent().unwrap().join("src").join("924.text");

    let all_lines = fh.readAndTokenizeInput();

    let mut i = 0;
    while i < all_lines.len() {
        let vertices = &all_lines[i];
        let malware = &all_lines[i + 1];
        i += 2;
        println!("For vertices = {:?} malware = {:?} answer is ", vertices, malware);
    }
}