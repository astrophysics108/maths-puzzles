
fn get_nums(num: String) {
    if num.len() < 9 {
        for i in 1..10 {
            let newnum_str = format!("{}{}", num, i);
            let newnum: i32 = newnum_str.parse().expect("Failed to parse");
            if newnum % ((num.len() + 1) as i32) == 0 && !num.contains(&i.to_string()) {
                get_nums(newnum_str);
            }
        }
    } else {
        let newnum = format!("{}0", num);
        println!("{}", newnum);
    }
}

fn main() {
    get_nums(String::new());
}
