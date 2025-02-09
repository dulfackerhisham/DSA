let n = 5;
let i = 1;

// for (let i=0;i<n; i++) {
//     console.log("* ".repeat(n))
// }

for (let i=0; i<n; i++) {
    let row = "";
    for (let j=0; j<n ; j++) {
        row += "* "
    }
    console.log(row)

}