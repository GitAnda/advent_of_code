const INPUT: &str = include_str!("day4.txt");

fn input() -> Vec<Vec<Vec<u32>>> {
    INPUT
        .lines()
        .map(|line| {
            line.split(",")
                .map(|range| {
                    range
                        .split("-")
                        .map(|value| value.parse().unwrap())
                        .collect::<Vec<u32>>()
                })
                .collect::<Vec<Vec<u32>>>()
        })
        // .map(|line| line.split(",").collect::<Vec<&str>>())
        .collect()
}

fn contains(range1: &Vec<u32>, range2: &Vec<u32>) -> u32 {
    if range1[0] <= range2[0] && range2[1] <= range1[1] {
        1
    } else if range2[0] <= range1[0] && range1[1] <= range2[1] {
        1
    } else {
        0
    }
}

#[test]
fn solve() {
    let data = input();
    // println!("{:?}", data);

    let res: u32 = data
        .iter()
        .map(|ranges| contains(&ranges[0], &ranges[1]))
        .collect::<Vec<u32>>()
        .iter()
        .sum();
    println!("Part 1: {:?}", res);

    let res = 0;
    println!("Part 2: {:?}", res);
}
