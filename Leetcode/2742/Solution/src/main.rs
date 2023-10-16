struct Solution {}

use std::cmp::min;
use std::cmp::max;
use std::cmp::Ordering;
use std::convert::TryInto;

// Priority Queue depends on Ord.
impl Ord for CostMin {
    fn cmp(&self, other: &Self) -> Ordering {
        let o_cost_per_time: f32 = (other.cost as f32) / (other.time as f32);
        let s_cost_per_time: f32 = (self.cost as f32) /(self.time as f32);
        // println!("other cost {:?} time {:?} self cost {:?} time {:?}\nother cost/time = {:?} self cost/time = {:?}", other.cost, other.time, self.cost, self.time, o_cost_per_time, s_cost_per_time);
        if s_cost_per_time > o_cost_per_time {
            return Ordering::Greater;
        } else if o_cost_per_time == s_cost_per_time {
            if self.time > other.time {
                return Ordering::Less;
            } else {
                return Ordering::Greater;
            }            
        } else {
            return Ordering::Less;
        }
    }
}

// `PartialOrd` needs to be implemented as well.
impl PartialOrd for CostMin {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

#[derive(PartialEq)]
#[derive(Eq)]
#[derive(Debug)]
struct CostMin {
    cost : i32,
    time : i32,
    original_time : i32,
    position : i32
}

impl Solution {
    pub fn paint_walls(mut cost: Vec<i32>, time: Vec<i32>) -> i32 {
        // The paid painter picks the wall with the lowest cost.
        // If there are more than one wall with lowest cost, pick
        // the one that takes more time.

        // let mut heap = BinaryHeap::new();        
        let total_size : i32 = cost.len().try_into().unwrap();

        let mut i : usize = 0;
        let mut sorted_container : Vec<CostMin> = vec![];
        while i < total_size.try_into().unwrap() {
            let mut painting_time : i32 = *time.get(i).unwrap();
            if painting_time > total_size {
                painting_time = total_size;
            }
            let to_push = CostMin {
                cost: *cost.get(i).unwrap(),
                time : painting_time + 1,
                original_time : *time.get(i).unwrap(),
                position : i.try_into().unwrap()};
            sorted_container.push(to_push);
            // println!("At index {} sorted container = {:?}", i, sorted_container);
            i += 1;
        }

        sorted_container.sort();

        println!("Sorted container before re-adjusting weights {:?}", sorted_container);

        let mut walls_remaining = total_size;
        for cost_struct in sorted_container.iter_mut() {
            if walls_remaining <= 0 {
                cost_struct.time = 1;
            } else if walls_remaining <= cost_struct.time {
                // Reduce the extraneous time.
                let extraneous_time = cost_struct.time - walls_remaining;
                cost_struct.time -= extraneous_time;
                cost_struct.time = max(cost_struct.time, 1);
            }
            walls_remaining = walls_remaining - (cost_struct.time);
        }

        sorted_container.sort();
        println!("Sorted container after re-adjusting weights {:?}", sorted_container);

        // Based on an element's position in the sorted order, we need to update its '(effective) time' value.
        let mut total_cost = 0;
        let mut remaining = total_size;
        let mut current: usize = 0;
        while remaining > 0 {
            let x = &sorted_container[current];
            println!("{:?} remaining = {}", x, remaining);
            total_cost += x.cost;
            current += 1;
            remaining = remaining - (1 + x.original_time);
        }
        total_cost
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
    //let cost : Vec<i32> = Vec::from([1,2,3,2]);
    //let time : Vec<i32> = Vec::from([1,2,3,2]);
    // let cost : Vec<i32> = Vec::from([26, 53, 10, 24, 25, 20, 107,51]);
    // Sorted order is 10, 20, 24, 25, 26, [51], [53], [63]
    //                   1  2   1   2   1   1   1   2
    // let time : Vec<i32> = Vec::from([1, 1, 1, 1, 2, 2, 3, 2]);
    // let cost : Vec<i32> = Vec::from([42,8,28,35,21,13,21,35]);
    // let time : Vec<i32> = Vec::from([2,1,1,1,2,1,1,2]);

    // let cost : Vec<i32> = Vec::from([49,35,32,20,30,12,42]);
    // let time : Vec<i32> = Vec::from([1,1,2,2,1,1,2]);
    let cost = Vec::from([76,25,96,46,85,19,29,88,2,5]);
    let time = Vec::from([1,2,1,3,1,3,3,3,2,1]);
    println!("input cost = {:?} time = {:?}", cost, time);
    println!("{}", Solution::paint_walls(cost, time));
    //}
}
