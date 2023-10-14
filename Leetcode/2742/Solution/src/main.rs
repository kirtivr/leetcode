struct Solution {}

impl Solution {
    pub fn paint_walls(cost: Vec<i32>, time: Vec<i32>) -> i32 {
        // The paid painter picks the wall with the lowest cost.
        // If there are more than one wall with lowest cost, pick
        // the one that takes more time.

        let cost_to_iter: std::collections::HashMap<i32, i32>;
        for i in [0..cost.len()] {
            cost_to_iter.insert(i, cost[i]);
        }
        let sorted_cost = cost;
        sorted_cost.sort();

        let i = 0;
        while i < sorted_cost.len() {
            let lowest = sorted_cost[i];

            let j = i + 1;
            while j < sorted_cost.len() {

            }
        }

        1
    }
}

use std::fs::File;
use std::io::prelude::*;
use std::path::PathBuf;

struct FileHandler {
    path : PathBuf,
}

impl FileHandler {
    fn tokenizeString(&self, s: String) -> Vec<String> {
        // We expect a list of comma separated values.
        // println!("{}", s);
        let r = s.replace(|ch| ch == '[' || ch == ']', "");
        let values : Vec<String> = r.split(',').map(String::from).collect();
        values
    }

    pub fn readAndTokenizeInput(&self) -> Vec<Vec<String>> {
        let s : String = self.readFileContents();

        let mut result = Vec::new();
        for line in s.lines() {
            result.push(self.tokenizeString(line.to_string()));
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
    /*let mut fh = FileHandler {
        path : PathBuf::new()
    };

    let path = std::env::current_exe().unwrap();
    fh.path = path.parent().unwrap().parent().unwrap().parent().unwrap().join("src").join("2742.text");

    for line in fh.readAndTokenizeInput() {
        let input: Vec<i32> = line.iter().map(|s| s.parse::<i32>().unwrap()).collect();
        println!("input = {:?}", input);
        for num in &input {
            println!("binary for {} is {:0b}", num, num)
        }*/
    let cost : Vec<i32> = Vec::from([1,2,3,2]);
    let time : Vec<i32> = Vec::from([1,2,3,2]);

    println!("{}", Solution::paint_walls(cost, time));
    //}
}
