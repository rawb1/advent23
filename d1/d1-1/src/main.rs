use std::env;
use std::fs;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let args: Vec<String> = env::args().collect();

    let file_path = &args[1];
    let mut result = Vec::new();
    for line in fs::read_to_string(file_path).unwrap().lines() {
        // find the first number string in the line
        let mut number = String::new();

        for (_i, c) in line.chars().enumerate() {
            if c.is_digit(10) {
                number.push(c);
                break;
            }
        }

        // find the last number in the line
        for (_i, c) in line.chars().rev().enumerate() {
            if c.is_digit(10) {
                number.push(c);
                break;
            }
        }

        result.push(number)
    }

    // add all the numbers together
    let mut sum = 0;
    for number in result {
        sum += number.parse::<i32>().unwrap();
    }

    // write the sum to a file
    let mut file = File::create("output.txt").unwrap();
    file.write_all(sum.to_string().as_bytes()).unwrap();
}
