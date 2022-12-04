use std::collections::HashSet;

const INPUT: &str = include_str!("day3.txt");

fn priority(c: char) -> u32 {
    if c.is_uppercase() {
        c as u32 - 65 + 27
    } else {
        c as u32 - 97 + 1
    }
}

fn input() -> Vec<Vec<u32>> {
    INPUT
        .lines()
        .map(|line| line.chars().map(priority).collect())
        // .map(|line| HashSet::from_iter(line.chars().map(|c| priority(c))))
        .collect()
}

fn intersect_two_bags(bag: &HashSet<u32>, other: &HashSet<u32>) -> HashSet<u32> {
    bag.intersection(other).copied().collect::<HashSet<u32>>()
}

fn intersect_bags(mut bags: Vec<HashSet<u32>>) -> HashSet<u32> {
    let mut intersection = bags.pop().unwrap();

    while !bags.is_empty() {
        let bag = bags.pop().unwrap();

        intersection = intersection.intersection(&bag).copied().collect();
    }

    intersection
}

#[test]
fn solve() {
    let data = input();
    let res: u32 = data
        .iter()
        .map(|bag| bag.split_at(bag.len() / 2))
        .map(|bag| {
            *bag.0
                .iter()
                .copied()
                .collect::<HashSet<u32>>()
                .intersection(&bag.1.iter().copied().collect::<HashSet<u32>>())
                .next()
                .unwrap()
        })
        .sum();
    println!("Part 1: {:?}", res);

    let res: u32 = data
        .chunks(3)
        .map(|chunk| {
            *intersect_bags(chunk
                .iter()
                .map(|v| v.iter().copied().collect::<HashSet<u32>>())
                .collect::<Vec<HashSet<u32>>>())
                .iter()
                .next()
                .unwrap()
        })
        .sum();
    println!("Part 2: {:?}", res);
}
