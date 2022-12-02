use std::collections::HashMap;

const INPUT: &str = include_str!("day2.txt");

fn input() -> Vec<Vec<u32>> {
    let to_int: HashMap<&str, u32> = HashMap::from([
        ("A", 1),
        ("X", 1),
        ("B", 2),
        ("Y", 2),
        ("C", 3),
        ("Z", 3),
    ]);

    INPUT
        .lines()
        .map(|line| {
            line.split(" ")
                .map(|value| *to_int.get(value).unwrap())
                .collect::<Vec<u32>>()
        })
        .collect::<Vec<Vec<u32>>>()
}

// fn points(them, me) -> u32 {
//     if me == them:
//         return 3 + me
//     else if me == WIN[them]:
//         return 6 + me
//     else:
//         return 0 + me
// }

#[test]
fn solve() {
    let mut rounds = input();
    println!("{:?}", rounds);
    // let mut rounds = input().
    //     .iter()
    //     .map(|round| round.iter().sum())
    //     .collect::<Vec<u32>>();
    // elfs.sort();
    // elfs.reverse();
    // println!("Part 1: {:?}", elfs.first().unwrap());
    // println!("Part 1: {:?}", elfs[0] + elfs[1] + elfs[2]);
}


