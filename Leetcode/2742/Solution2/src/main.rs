struct Solution {}

use core::time;
use std::borrow::BorrowMut;
use std::cmp::min;
use std::cmp::max;
use std::cmp::Ordering;
use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::btree_set::Union;
use std::convert::TryInto;
use std::ops::Add;
use std::ops::AddAssign;
use std::rc::Rc;

// Priority Queue depends on Ord.
/*impl Ord for CostMin {
    fn cmp(&self, other: &Self) -> Ordering {
        return self.time.cmp(&other.time);
    }
}

// `PartialOrd` needs to be implemented as well.
impl PartialOrd for CostMin {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}*/

const TEMP_ID: i32 = -2;
const WALL_ID: i32 = 1000;
const INVALID: i32 = -3;

#[derive(PartialEq)]
#[derive(Eq)]
#[derive(Debug)]
#[derive(Hash)]
#[derive(Clone)]
#[derive(Default)]
struct TimeRange {
    id : i32,
    low : i32,
    high : i32,
    cost : i32
}

#[derive(PartialEq)]
#[derive(Eq)]
#[derive(Debug)]
#[derive(Clone)]
#[derive(Default)]
struct UnionRange {
    range: TimeRange,
    uses_ranges: HashSet<i32>,
}

impl Solution {

fn extract_cost_from_vec(lowest_cost_for_time: &Vec<UnionRange>, time_left: i32) -> Option<&UnionRange> {
    for time_cost_range in lowest_cost_for_time.iter() {
        let (ltime, htime, cost) = (time_cost_range.range.low, time_cost_range.range.high, time_cost_range.range.cost);
        if time_left >= ltime && time_left <= htime {
            return Some(time_cost_range);
        }
    }
    return None;
}

fn zero_one_knapsack_recurse<'a>(
    lowest_cost_for_time: &mut Vec<UnionRange>, walls: &'a HashSet<TimeRange>, time_left : i32, visited: &mut HashSet<i32>, id: &mut i32) -> 
    HashSet<TimeRange> {
    // println!("visited = {:?} time_left = {}", visited, time_left);

    for time_cost_range in lowest_cost_for_time.iter() {
        if visited.contains(&time_cost_range.range.id) {
            continue;
        }
        let mut invalid = false;
        for range_id in time_cost_range.uses_ranges.iter() {
            if visited.contains(range_id) {
                invalid = true;
                break;
            }
        }
        if invalid {
            continue;
        }
        let (ltime, htime, _cost) = (time_cost_range.range.low, time_cost_range.range.high, time_cost_range.range.cost);
        if time_left >= ltime && time_left <= htime {
            // We know that in this range of time, this is the minimum cost.
            for range_id in time_cost_range.uses_ranges.iter() {
                visited.insert(*range_id);
            }
            visited.insert(time_cost_range.range.id);
            return Default::default();
        }
    }


    let mut to_remove_walls: HashSet<TimeRange> = Default::default();
    let mut output_tr: UnionRange = Default::default();
    output_tr.range.id = TEMP_ID;
    output_tr.range.cost = i32::pow(10, 9);
    for wall in walls.iter() {
        if wall.high >= time_left {
            if wall.cost < output_tr.range.cost {
                to_remove_walls.clear();
                to_remove_walls.insert(wall.clone());
                output_tr.range.low = time_left;
                output_tr.range.high = wall.high;
                output_tr.range.cost = wall.cost;
            }
        }
    }

    let mut newline: bool = false;
    for pointer in 1..time_left {
        let a_part = pointer;
        let b_part = time_left - pointer;
        let a_to_remove = Self::zero_one_knapsack_recurse(lowest_cost_for_time, walls, a_part, visited, id);
        let mut to_send : HashSet<TimeRange> = Default::default();
        for x in walls.difference(&a_to_remove) {
            to_send.insert(x.clone());
        }
        // println!("visited = {:?} walls_to_remove = {:?}", visited, a_to_remove);
        let b_to_remove = Self::zero_one_knapsack_recurse(lowest_cost_for_time, &to_send, b_part, visited, id);
        let a_cost = Self::extract_cost_from_vec(lowest_cost_for_time, a_part).unwrap();
        let b_cost = Self::extract_cost_from_vec(lowest_cost_for_time, b_part).unwrap();

        println!("a part = {} cost = {} b part = {} cost = {}", a_part, b_part, a_cost.range.cost, b_cost.range.cost);
        if a_cost.range.cost + b_cost.range.cost < output_tr.range.cost {
            newline = true;
            output_tr.range.cost = a_cost.range.cost + b_cost.range.cost;
            output_tr.range.low = time_left;
            output_tr.range.high = a_cost.range.high + b_cost.range.high;
            output_tr.uses_ranges.clear();
            for x in a_cost.uses_ranges.union(&b_cost.uses_ranges) {
                output_tr.uses_ranges.insert(*x);
            }
            for x in visited.iter() {
                output_tr.uses_ranges.insert(*x);
            }
            println!("time_left = {} min is from {} and {} a_TimeRange = {:?} b_TimeRange = {:?}",time_left, a_part, b_part, a_cost, b_cost);
            to_remove_walls.clear();
            for x in a_to_remove.union(&b_to_remove) {
                to_remove_walls.insert(x.clone());
            }
        }
        visited.clear();
    }

    // So our input time was "time_left" but the minimum cost here covers a range up to min_cost.time.
    if (Self::extract_cost_from_vec(lowest_cost_for_time, time_left).is_none()) {
        *id += 1;
        lowest_cost_for_time.push(
            UnionRange {
                range : TimeRange {
                id : *id,
                low : output_tr.range.low,
                high : output_tr.range.high,
                cost : output_tr.range.cost
            },
            uses_ranges : output_tr.uses_ranges.clone(),
        });
    }
    if newline {
        println!("\n");
    }
    return to_remove_walls;
}


fn zero_one_knapsack_iterative(
    mut sorted_container : &mut HashSet<TimeRange>, mut id: &mut i32) -> i32
{
    let n: i32 = sorted_container.len().try_into().unwrap();
    let mut lowest_cost_for_time: Vec<UnionRange> = Default::default();


    let mut visited: HashSet<i32> = Default::default();
    let mut time_left = 1;
    let mut time_elapsed = 0;
    while time_left <= n {
        // println!("[{}][{}]", current, remaining);
        let walls_painted =
        Self::zero_one_knapsack_recurse(&mut lowest_cost_for_time, &mut sorted_container, time_left, &mut visited, &mut id);
        let mut copy: HashSet<TimeRange> = Default::default();
        for x in walls_painted {
            copy.insert(x.clone());
        }
        println!("\nto remove = {:?}", copy);

        sorted_container.retain(|wall| {
            return !(copy.contains(wall));
        });
        println!("for time = {} \nlowest costs = {:?}\n", time_left, lowest_cost_for_time);
        // Can clear the "visited" set here, because we can reuse groups.
        visited.clear();

        time_left += 1;
        println!("time left = {}", time_left);
    }
    
    for time_cost_range in lowest_cost_for_time.iter() {
        let (ltime, htime, _cost) = (time_cost_range.range.low, time_cost_range.range.high, time_cost_range.range.cost);
        if n >= ltime && n <= htime {
            return time_cost_range.range.cost;
        }
    }
    return 0;
}

pub fn paint_walls(mut cost: Vec<i32>, time: Vec<i32>) -> i32 {
        // The paid painter picks the wall with the lowest cost.
        // If there are more than one wall with lowest cost, pick
        // the one that takes more time.
        let total_size : i32 = cost.len().try_into().unwrap();

        let mut i : usize = 0;
        let mut sorted_container : HashSet<TimeRange> = Default::default();
        let mut id: i32 = WALL_ID;
        while i < total_size.try_into().unwrap() {
            let mut painting_time : i32 = *time.get(i).unwrap();
            if painting_time > total_size {
                painting_time = total_size;
            }
            id += 1;
            let to_push = TimeRange {
                id : id,
                cost: *cost.get(i).unwrap(),
                low : painting_time + 1,
                high : painting_time + 1,
            };
            sorted_container.insert(to_push);
            // println!("At index {} sorted container = {:?}", i, sorted_container);
            i += 1;
        }

        println!("Sorted container {:?}", sorted_container);

        // return Self::zero_one_knapsack(&sorted_container, 0, 0, total_size, &mut visited).unwrap();
        id = 0;
        return Self::zero_one_knapsack_iterative(&mut sorted_container, id.borrow_mut());
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
    let cost : Vec<i32> = Vec::from([26, 53, 10, 24, 25, 20, 107,51]);
    // Sorted order is 10, 20, 24, 25, 26, [51], [53], [63]
    //                   1  2   1   2   1   1   1   2
    let time : Vec<i32> = Vec::from([1, 1, 1, 1, 2, 2, 3, 2]);
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
    // let cost = Vec::from([7,15,38,35,61,90,34,29,68,35]);
    // let time = Vec::from([1,1,3,3,2,1,3,1,2,3]);
    println!("input cost = {:?} time = {:?}", cost, time);
    println!("{}", Solution::paint_walls(cost, time));
    //}
}
