const INPUT: &str = include_str!("day1.txt");

fn input() -> Vec<Vec<u32>> {
    INPUT
        .split("\r\n\r\n")
        .map(|line| {
            line.split("\r\n")
                .map(|value| value.parse().unwrap())
                .collect::<Vec<u32>>()
        })
        .collect::<Vec<Vec<u32>>>()
}

#[test]
fn solve() {
    let mut elfs = input()
        .iter()
        .map(|elf| elf.iter().sum())
        .collect::<Vec<u32>>();
    elfs.sort();
    elfs.reverse();
    println!("Part 1: {:?}", elfs.first().unwrap());
    println!("Part 1: {:?}", elfs[0] + elfs[1] + elfs[2]);
}
