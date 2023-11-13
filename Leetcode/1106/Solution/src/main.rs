struct Solution {}

impl Solution {
    fn and_expr(symbols: &Vec<char>) -> bool {
        let mut out = true;
        for sym in symbols {
            let mut opd = false;
            if *sym == 't' {
                opd = true;
            }
            out = out & opd;
        }
        return out;
    }

    fn or_expr(symbols: &Vec<char>) -> bool {
        let mut out = false;
        for sym in symbols {
            let mut opd = false;
            let tc: char = 't';
            if *sym == tc {
                opd = true;
            }
            out = out || opd;
        }
        return out;        
    }

    fn not_expr(sym: char) -> bool {
        if sym == 'f' {
            return true;
        }
        return false;
    }

    fn apply_operator(popped_symbols: &Vec<char>, operator: char) -> char {
        let mut result: bool = false;
        if operator == '&' {
            result = Self::and_expr(popped_symbols);
        } else if operator == '|' {
            result = Self::or_expr(popped_symbols);
        } else if operator == '!' {
            if popped_symbols.len() > 1 {
                println!("! operator can only take one operand");
            }
            result = Self::not_expr(popped_symbols[0]);
        }

        if result {
            return 't';
        }
        return 'f';
    }

    pub fn parse_bool_expr(expression: String) -> bool {
        // An expression is bounded between parantheses.
        // Iterate through the expression, adding symbols to the stack until we see a closing parantheses.
        // Pop symbols until we find an opening parantheses.
        // Evaluate the popped symbols. Push the result of the evaluation to the stack, if there are remaining
        // symbols in the expression. Else, return the result.
        let mut stk : Vec<char> = Vec::with_capacity(expression.len());

        for i in 0..expression.len() {
            let ch: char = expression.as_bytes()[i] as char;

            if ch == ')' {
                // Pop elements from the stack until we find an opening brace.
                let mut popped_symbols: Vec<char> = Default::default();
                while stk.len() > 0 {
                    let popped = stk.pop().unwrap();
                    if popped == '(' {
                        break;
                    }
                    popped_symbols.push(popped);
                }
                // What is the operator to be applied.
                let operator: char = stk.pop().unwrap();
                stk.push(Self::apply_operator(&popped_symbols, operator));
            }
            stk.push(ch);
        }
        if stk.pop().unwrap() == 't' {
            return true;
        }
        return false;
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
    fh.path = path.parent().unwrap().parent().unwrap().parent().unwrap().join("src").join("1106.text");

    let all_lines = fh.readAndTokenizeInput();

    for i in 0..all_lines.len() {
        let s = &all_lines[i];
        println!("s = {:?}", s);
        //println!("For s = {:?} answer is {}", s, Solution::parse_bool_expr(s.clone()));
    }
}