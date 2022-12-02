use std::collections::HashMap;

const INPUT: &str = include_str!("day2.txt");
const WIN: [i32; 3] = [2, 3, 1];
const LOSE: [i32; 3] = [3, 1, 2];

fn input() -> Vec<Vec<i32>> {
    let to_int: HashMap<&str, i32> =
        HashMap::from([("A", 1), ("X", 1), ("B", 2), ("Y", 2), ("C", 3), ("Z", 3)]);

    INPUT
        .lines()
        .map(|line| {
            line.split(" ")
                .map(|value| *to_int.get(value).unwrap())
                .collect::<Vec<i32>>()
        })
        .collect::<Vec<Vec<i32>>>()
}

fn points(them: i32, me: i32) -> i32 {
    if me == them {
        3 + me
    } else if me == WIN[(them - 1) as usize] {
        6 + me
    } else {
        0 + me
    }
}

fn play(them: i32, outcome: i32) -> i32 {
    if outcome == 2 {
        them
    } else if outcome == 1 {
        LOSE[(them - 1) as usize]
    } else {
        WIN[(them - 1) as usize]
    }
}

#[test]
fn solve() {
    let p: i32 = input()
        .iter()
        .map(|round| points(round[0], round[1]))
        .collect::<Vec<i32>>()
        .iter()
        .sum();
    println!("Part 1: {:?}", p);

    let p: i32 = input()
        .iter()
        .map(|round| points(round[0], play(round[0], round[1])))
        .collect::<Vec<i32>>()
        .iter()
        .sum();
    println!("Part 2: {:?}", p);
}
