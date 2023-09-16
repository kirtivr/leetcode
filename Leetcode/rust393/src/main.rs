struct Solution {}

impl Solution {
    pub fn bytes_to_read_given_preamble(preamble: i32) -> Result<usize, &'static str> {
        // Return the number of consecutive ones starting from the MSB to the LSB.
        let mut msb_position = 7;
        let mut count : usize = 0;

        while msb_position >= 0 {
            let and_number = 1 << msb_position;
            let is_set = and_number & preamble > 0;
            if !is_set {
                break;
            }
            count += 1;
            msb_position -= 1;
        }
        // println!("preamble {} count is {}", preamble, count);
        if count == 0 {
            Ok(1)
        } else if count == 1 {
            // Invalid.
            Result::Err("Only the MSB bit is set.")
        } else if count > 4 {
            Result::Err("More than 4 MSBs set in preamble.")
        } else {
            Ok(count)
        }
    }

    pub fn valid_utf8(data: Vec<i32>) -> bool {
        let mut i = 0;

        while i < data.len() {
            let preamble : i32 = data[i];
            // println!("{:#?}", preamble);

            let result_or_bytes_to_validate = Solution::bytes_to_read_given_preamble(preamble);
            if !result_or_bytes_to_validate.is_ok() {
                return false;
                // println!("Something wrong with the preamble {:032b}", preamble);
            }

            let bytes_to_validate = result_or_bytes_to_validate.unwrap();

            if bytes_to_validate == 1 {
                // Note this includes the already validated preamble.
                i += 1;
                continue;
            }

            // Invalid number of bytes to be validated.
            // Note bytes to validate includes i.
            if i + bytes_to_validate - 1 >= data.len() {
                // println!("Given preamble {:032b} bytes to validate = {} i = {} overflows data with length {}", preamble, bytes_to_validate, i, data.len());
                return false;
            }

            // Validate all the bytes.
            for j in i+1..i+bytes_to_validate {
                let byte : i32 = data[j];

                let first_two_bits : i32 = 0xC0 & byte;
                if first_two_bits != 0x80 {
                    // println!("failed to validate bytes. first two bits = {} byte = {}", first_two_bits, byte);
                    return false;
                } else {
                    // println!("validated bytes. first two bits = {} byte = {}", first_two_bits, byte);
                }
            }

            i = i + bytes_to_validate;
        }
        return true;
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
    let mut fh = FileHandler {
        path : PathBuf::new()
    };

    let path = std::env::current_exe().unwrap();
    fh.path = path.parent().unwrap().parent().unwrap().parent().unwrap().join("src").join("393.text");

    for line in fh.readAndTokenizeInput() {
        let input: Vec<i32> = line.iter().map(|s| s.parse::<i32>().unwrap()).collect();
        println!("input = {:?}", input);
        for num in &input {
            println!("binary for {} is {:0b}", num, num)
        }
        println!("{}", Solution::valid_utf8(input));
    }
}
