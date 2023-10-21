struct Solution {}

use std::cmp::min;
use std::cmp::max;
use std::cmp::Ordering;
use std::collections::HashMap;
use std::convert::TryInto;

// Priority Queue depends on Ord.
impl Ord for CostMin {
    fn cmp(&self, other: &Self) -> Ordering {
        let o_cost_per_time: f32 = (other.cost as f32) / (other.time as f32);
        let s_cost_per_time: f32 = (self.cost as f32) / (self.time as f32);
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
/*     fn zero_one_knapsack(
        sorted_container : &Vec<CostMin>, mut current : usize, mut total_cost : i32,
        mut remaining : i32, mut visited : &mut HashMap<(i32, i32), i32>) -> Option<i32> 
{        
    let container_size = sorted_container.len();
    let preceding_cost = total_cost;

    if current == container_size {
        return None
    }

    let visited_index: (i32, i32) = (current.try_into().unwrap(), remaining);
    if visited.contains_key(&visited_index) {
        return Some(visited[&visited_index] + total_cost);
    }
    
    let mut min_cost = i32::pow(10, 9);
    while remaining > 0 && current < container_size{
        // Either the current element is picked or it is not picked.
        let x = &sorted_container[current];
        let cost_if_skipped = Self::zero_one_knapsack(&sorted_container, current + 1, total_cost, remaining, &mut visited);
        if cost_if_skipped.is_some() {
            min_cost = min(min_cost, cost_if_skipped.unwrap());
        }
        // println!("painting wall {:?} remaining = {}", x, remaining);
        total_cost += x.cost;
        current += 1;
        remaining = remaining - (1 + x.original_time);
    }

    if remaining <= 0 {
        min_cost = min(min_cost, total_cost);
        visited.insert((visited_index.0, visited_index.1), min_cost - preceding_cost);
    }
    if min_cost == i32::pow(10, 9) {
        return None;
    }
    return Some(min_cost)
}*/

fn zero_one_knapsack_inner(
    sorted_container : &Vec<CostMin>, mut current : usize,
    mut remaining : i32, visited : &mut HashMap<(i32, i32), Option<i32>>) {
        let container_size = sorted_container.len();
    
        if current == container_size {
            return;
        }
    
        let visited_index: (i32, i32) = (current.try_into().unwrap(), remaining);
        if visited.contains_key(&visited_index) {
            return;
        }    

        let mut min_cost = i32::pow(10, 9);
        let mut total_cost = 0;
        while remaining > 0 && current < container_size {
            // Either the current element is picked or it is not picked.
            let temp : usize = (remaining + 1).try_into().unwrap();            
            if current + 1 < container_size && ((current + temp < container_size)) {
                let cost_if_skipped = visited[&((current + 1).try_into().unwrap(), remaining)];
                if cost_if_skipped.is_some() {
                    min_cost = min(min_cost, total_cost + cost_if_skipped.unwrap());
                }
            }  

            // println!("painting wall {:?} remaining = {}", x, remaining);
            let x = &sorted_container[current];
            total_cost += x.cost;
            current += 1;
            remaining = remaining - (1 + x.original_time);
        }

        if remaining <= 0 {
            // println!("visited {:?} total cost = {} min cost = {}", visited_index, total_cost, min_cost);
            min_cost = min(min_cost, total_cost);
            visited.insert((visited_index.0, visited_index.1), Some(min_cost));
        } else if min_cost == i32::pow(10, 9) {
            visited.insert((visited_index.0, visited_index.1), None);
        } else {
            visited.insert((visited_index.0, visited_index.1), Some(min_cost));
        }

        return;
    }

fn zero_one_knapsack_iterative(
    sorted_container : &Vec<CostMin>, mut visited : &mut HashMap<(i32, i32), Option<i32>>)
{
    let N: i32 = sorted_container.len().try_into().unwrap();
    for current in (0..N).rev() {
        for remaining in (0..N + 1).rev() {
            // println!("[{}][{}]", current, remaining);
            Self::zero_one_knapsack_inner(sorted_container, current.try_into().unwrap(), remaining.try_into().unwrap(), &mut visited);
            // println!("{:?}", visited);
        }
    }
}

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

        /*let mut walls_remaining = total_size;
        for cost_struct in sorted_container.iter_mut() {
            if walls_remaining <= 0 {
                cost_struct.time = 1;
            } else if walls_remaining < cost_struct.time {
                // Reduce the extraneous time.
                let extraneous_time = cost_struct.time - walls_remaining;
                cost_struct.time -= extraneous_time;
            }
            walls_remaining = walls_remaining - (cost_struct.time);
        }

        sorted_container.sort();
        println!("Sorted container after re-adjusting weights {:?}", sorted_container);
        */
        let mut visited:HashMap<(i32, i32), Option<i32>> = Default::default();

        // return Self::zero_one_knapsack(&sorted_container, 0, 0, total_size, &mut visited).unwrap();

        Self::zero_one_knapsack_iterative(&sorted_container, &mut visited);

        // println!("{:?}", visited);
        println!("[2][10] = {} [3][6] = {} [0][2] = {}", visited[&(3, 10)].unwrap(), visited[&(4, 6)].unwrap(), visited[&(0, 2)].unwrap());
        return visited[&(0, total_size)].unwrap();
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
    // let cost : Vec<i32> = Vec::from([1,2,3,2]);
    // let time : Vec<i32> = Vec::from([1,2,3,2]);
    // let cost : Vec<i32> = Vec::from([26, 53, 10, 24, 25, 20, 107,51]);
    // Sorted order is 10, 20, 24, 25, 26, [51], [53], [63]
    //                   1  2   1   2   1   1   1   2
    // let time : Vec<i32> = Vec::from([1, 1, 1, 1, 2, 2, 3, 2]);
    // let cost : Vec<i32> = Vec::from([42,8,28,35,21,13,21,35]);
    // let time : Vec<i32> = Vec::from([2,1,1,1,2,1,1,2]);

    // let cost : Vec<i32> = Vec::from([49,35,32,20,30,12,42]);
    // let time : Vec<i32> = Vec::from([1,1,2,2,1,1,2]);
    // let cost = Vec::from([76,25,96,46,85,19,29,88,2,5]);
    // let time = Vec::from([1,2,1,3,1,3,3,3,2,1]);
    // let cost = Vec::from([937,252,716,781,319,198,273,554,140,68,694,583,1080,16,450,229,710,1003,1117,1036,398,874,289,664,600,588,372,1066,375,532,984,328,1067,746]);
    // let time = Vec::from([5,3,1,3,2,1,3,3,5,3,5,5,4,1,3,1,4,4,4,1,5,1,2,3,2,3,3,4,1,3,4,1,1,5]);
    //let cost = Vec::from([41675,90161,42520,2465,108823,98591,49224,46555,131321,216747,7258,6299,169312,168482,130148,226209,197115,15146,55089,187926,78480,111029,149448,67732,54628,196939,25374,194820,14127,85198,97214,134385,56194,238827,35900,121819,208957,107083,238577,150903,126509,76669,60955,46842,158083,116031,32064,63773,120096,216182,153556,34298,145897,157373,78292,176632,159220,18749,224908,12650,232288,62610,5937,34619,99324,66938,213520,94116,133113,234093,202342,42557,170595,77540,40425,240793,136442,185747,19610,1279,126431,139526,140677,69081,119353,139199,55915,8350,107974,27172,180275,81994,162221,238364,218745,125032,110797,236061,125937,127927,186660,122670,132524,122477,126795,67347,48530,89577,125199,18530,214409,174298,74254,235,156489,209119,204785,175568,59549,82607,211991,153185,49666,129143,80511,33293,164404,229008,123974,226738,181846,62761,231278,79167,151166,187715,161615,207109,129906,167893,136182,42894,187370,39969,6743,9406,199895,16024,52868,119138,33884,170451,90106,23158,213806,193552,220162,223579,145187,72824,123924,103909,156478,105241,191831,125762,22026,213135,208691,139492,53292,216124,70708,1650,14223,146834,221897,2983,176816,142592,365,210600,92797,31105,140385,235568,16988,227990,87410,241067,229219,29455,235095,206722,33067,173429,173335,138607,195264,8718,180069,89331,82087,99767,210593,139259,230628,107238,69270,205825,222129,177425,233530,49351,55857,114637,80212,154839,152,12556,48684,18577,59045,242480,179325,165081,60876,170269,200253,13845,52579,209733,71088,223880,153760,107584,158823,68056,149410,112971,189975,229610,198299,116694,132896,236773,86703,230248,60016,16671,110518,165120,104334,111329,167568,58512,200481,105990,184663,158805,209591,159629,242966,217879,188151,36999,235805,3040,228087,145443,194727,227111,73716,60646,79701,77113,100063,122301,177805,115432,143504,105642,175829,223260,196590,209454,207756,15755,74830,184973,43249,4335,207433,83486,78888,172208,95841,237159,6382,170429,222212,153605,104335,207908,53476,151336,210360,49543,22342,232660,38247,178316,204946,99128,45026,102119,28955,119544,36304,98984,2378,224462,2305,158430,54224,67209,99644,175093,192855,63489,64096,215267,1162,219501,68560,216480,75965,18008,224154,59903,9444,75839,106329,20074,94729,183253,89182,218736,174058,216584,212835,173260,105726,184756,62870,94841,140979,30982,67675,84299,184896,163217,68378,227342,174141,138283,145291,216402,203876,109546,11123,37547,84335,207552,19054,146820,37754,124850,56560,85718,158882,138056,90513,17456,123409,9271,152276,56958,182559,177419,202995,211580,77668,208993,34950,168743,237430,146632,242385,94324,231793,104808,178101,19059,66441,19733,119659,95080,80720,138340,72267,182732,69323,32725,90967,148902,105132,64905,31616,185103,201046,40202,166635,226570,218536,140330,35,196762,211915,57942,139265,60002,200736,95740,160796,236401,114280,167988,26025,110206,13512,217865,52810,188783,103021,90155,30072,148118,132774,85351,217795,204933,53529,107626,41846,171335,142552,112932,208198,44216,6714,219388,142762,214524,59268,213010,213414,140124,83024,92851,143747,73179,219038,185261,100400,190972,46915,107024,83017,64933,185057,162001,208512,24871,21833,99141,93583,170977,118049,53297,111963,91506,23054]);
    // let time = Vec::from([7,2,6,5,4,1,10,6,6,7,2,10,2,7,10,7,7,2,9,6,8,8,10,5,4,1,2,6,1,6,7,10,2,3,8,3,10,3,3,8,2,5,4,4,1,7,1,4,10,8,3,8,3,5,6,3,5,10,4,10,4,6,9,1,4,8,9,5,8,7,4,2,3,4,7,8,10,4,6,10,5,5,10,1,9,3,4,6,6,8,7,10,10,9,9,6,8,1,6,6,5,4,6,8,7,4,6,1,8,7,3,7,2,2,2,1,7,10,8,3,3,5,7,6,4,8,4,9,1,9,7,10,7,1,2,8,7,6,5,2,9,7,8,2,4,4,3,4,7,10,3,7,4,9,6,9,5,2,4,9,10,9,7,7,3,4,1,6,2,4,7,6,10,2,4,8,7,7,6,7,8,9,10,4,9,1,8,4,2,6,3,4,2,6,1,9,7,8,8,10,9,4,3,6,5,4,10,7,7,8,3,10,5,3,6,6,9,3,5,8,2,1,7,5,6,4,4,7,9,7,5,4,1,5,3,2,2,3,1,10,10,1,10,10,3,10,4,3,7,6,4,4,1,2,10,8,8,3,1,4,2,1,6,1,10,6,6,4,6,10,3,10,1,4,3,8,6,9,6,6,6,3,9,2,6,4,2,5,10,1,3,2,4,10,3,4,1,9,6,8,3,6,6,6,6,4,7,5,1,5,9,10,3,1,8,4,4,6,3,10,4,8,6,6,8,5,3,6,1,8,5,8,9,5,6,8,5,2,2,3,5,5,7,4,2,3,4,4,10,1,6,2,2,2,6,8,1,2,1,3,10,1,5,2,6,4,2,2,3,9,7,10,3,4,9,9,3,6,9,9,1,3,8,3,9,1,1,7,1,10,4,5,5,4,8,5,5,2,3,9,10,8,2,7,10,4,2,5,4,8,3,8,2,6,5,6,7,4,2,4,5,5,4,9,3,8,1,1,10,5,2,4,7,7,10,2,6,4,8,1,8,1,6,9,6,8,5,3,9,4,5,8,3,3,3,3,4,7,4,6,5,4,8,7,1,6,9,4,3,4,8,10,8,10,8,3,8,2,3,10,2,2,1,2,6,3,3,4,9,9,5,8,2]);
    let cost = Vec::from([7,15,38,35,61,90,34,29,68,35]);
    let time = Vec::from([1,1,3,3,2,1,3,1,2,3]);
    println!("input cost = {:?} time = {:?}", cost, time);
    println!("{}", Solution::paint_walls(cost, time));
    //}
}
