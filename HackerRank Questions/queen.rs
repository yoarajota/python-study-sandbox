// Enter your code here 

fn display_path_to_princess(size: i32, matriz: Vec<&str>) {
    let mut princess = (0, 0);
    let mut bot = (0, 0);

    for (i, row) in matriz.iter().enumerate() {
        for (j, cell) in row.chars().enumerate() {
            if cell == 'p' {
                princess = (i as i32, j as i32);
            } else if cell == 'm' {
                bot = (i as i32, j as i32);
            }
        }
    }

    // calculate the difference between the bot and the princess
    let (diff_x, diff_y) = (princess.0 - bot.0, princess.1 - bot.1);

    println!("princess: {:?}, bot: {:?}", princess, bot);
    println!("diff_x: {}, diff_y: {}", diff_x, diff_y);

    // move the bot to the princess
    for _ in 0..diff_x.abs() {
        if diff_x > 0 {
            println!("DOWN");
        } else {
            println!("UP");
        }
    }

    for _ in 0..diff_y.abs() {
        if diff_y > 0 {
            println!("RIGHT");
        } else {
            println!("LEFT");
        }
    }
}

fn main() {
    display_path_to_princess(3, vec!["----", "-p--", "----", "--m-"]);
}