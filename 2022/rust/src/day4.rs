const INPUT: &str = include_str!("day4.txt");

fn input() -> Vec<Vec<&'static str>> {
    INPUT
        .lines()
        .map(|line| line.split(",").collect::<Vec<&str>>())
        .collect()
}

#[test]
fn solve() {
    let data = input();
    println!("{:?}", data);

    let res = 0;
    println!("Part 1: {:?}", res);

    let res = 0;
    println!("Part 2: {:?}", res);
}
