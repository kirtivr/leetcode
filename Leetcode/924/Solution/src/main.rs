struct Solution {}

use std::collections::{HashSet, HashMap};
use std::convert::TryInto;

impl Solution {
    fn do_traversal_from(start: i32, connections: &HashMap<i32, Vec<i32>>) -> HashSet<i32> {
        let mut stk: Vec<i32> = vec![start];
        let mut out: HashSet<i32> = Default::default();

        while stk.len() > 0 {
            let top = stk.pop().unwrap();

            if !connections.contains_key(&top) {
                continue;
            }

            for node in &connections[&top] {
                if *node != top && !out.contains(node){
                    out.insert(*node);
                    stk.push(*node);
                }  
             }
             //println!("stk = {:?}", stk);
        }

        return out;
    }
    fn retain_savable_nodes(start: i32, components: &mut HashSet<i32>, infected: &Vec<i32>) {
        let mut num_infected = 0;
        for v in components.iter() {
            if infected.contains(v) {
                num_infected += 1;
            }
        }
        components.retain(|v| !infected.contains(v));
        if num_infected <= 1 {
            components.insert(start);
        }
    }

    pub fn min_malware_spread(graph: Vec<Vec<i32>>, initial: Vec<i32>) -> i32 {
        let mut connections: HashMap<i32, Vec<i32>> = Default::default();
        for i in 0..graph.len() {
            for j in 0..graph[i].len() {
                let i_32 = i.try_into().unwrap();
                let j_32 = j.try_into().unwrap();
                if graph[i][j] == 0 || i == j {
                    continue;
                }
                if connections.contains_key(&i_32) {
                    connections.get_mut(&i_32).unwrap().push(j_32);
                } else {
                    connections.insert(i_32, vec![j_32]);
                }
            }
        }
        println!("connections: {:?} ", connections);

        // Find all connected components in the graph.
        let mut connected_components: HashMap<i32, HashSet<i32>> = Default::default();
        for start in &initial {
            let mut components = Self::do_traversal_from(*start, &connections);
            Self::retain_savable_nodes(*start, &mut components, &initial);
            println!("for start = {} connected = {:?}", *start, components);
            connected_components.insert(*start, components);
        }

        let mut max_inf = (0, i32::pow(10, 9));
        for (start, infected) in &connected_components {
            println!("with start = {} components: {:?}", *start, infected);
            if infected.len() > max_inf.0 || max_inf.0 == infected.len() && max_inf.1 > *start {
                max_inf = (infected.len(), *start);
            }    
        }

        max_inf.1
    }
}

use std::fs::File;
use std::io::prelude::*;
use std::path::PathBuf;

struct FileHandler {
    path : PathBuf,
}

impl FileHandler {
    fn tokenizeString(&self, s: &mut String) -> Vec<Vec<i32>> {
        // We expect a list of comma separated values.
        // println!("{}", s);
        s.retain(|ch| ch != '\"' && ch != ' ' && ch != '[');
        let mut arrays: Vec<String> = s.split(']').map(|x| String::from(x)).collect();
        arrays.retain(|group| group.len() > 0);
        //println!("arrays = {:?} s = {:?}", arrays, s);
        let mut out: Vec<Vec<i32>> = Default::default();
        for a in arrays {
            let mut values : Vec<i32> = a.split(',').map(|x| x.parse::<i32>().unwrap_or(-1)).collect();
            values.retain(|num| *num != -1);
            out.push(values);
        }
        out.retain(|group| group.len() > 0);
        //println!("out = {:?}", out);
        out
    }

    pub fn readAndTokenizeInput(&self) -> Vec<Vec<Vec<i32>>> {
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
        let vertices = all_lines[i].clone();
        let malware = all_lines[i + 1][0].clone();
        i += 2;
        println!("For vertices = {:?} malware = {:?} answer is {}", vertices, malware, Solution::min_malware_spread(vertices.clone(), malware.clone()));
    }
}