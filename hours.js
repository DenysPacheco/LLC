let h = 00
let m = 00
// let c = 0
// let flag = true
// if form a sequence sorted ex: 00:00 | 0,0,0,0
let count = 0
// if form a sequence crescent no repetitions sorted ex: 01:32 | 0,1,2,3
let countUnique = 0
// if form a sequence crescent no repetitions unsorted ex: 01:23 | 0,1,2,3
let countUltraUnique = 0

const fs = require("fs")

try {
    // Clear file content
    fs.truncateSync("./hours.log", 0, function () {
        console.log("File content cleared!")
    })
} catch (err) {
    console.log(err)
}

function log(content) {
    try {
        fs.appendFileSync(
            "./hours.log",
            content + "\n",
            { flag: "a+" },
            (err) => {},
        )

        //file written successfully
    } catch (err) {
        console.error(err)
    }
}

for (m = 0, h = 0; h < 23 || m < 60; m++) {
    if (m == 60) {
        h++
        m = 0
    }

    sh = h < 10 ? "0" + h.toString() : h.toString()
    sm = m < 10 ? "0" + m.toString() : m.toString()

    const ruleEqual = (curr, index, arr) => {
        return curr == arr[index + 1]
    }

    const ruleOneMore = (curr, index, arr) => {
        // Prox equals my current plus one
        // Crescent
        return curr == arr[index + 1] - 1
    }

    const ruleOneLess = (curr, index, arr) => {
        // Prox equals my current minus one
        // Decrescent
        return curr == arr[index + 1] + 1
    }

    const ruleIndexOut = (curr, index, arr) => {
        return index === arr.length - 1
    }

    rules = {
        count: (curr, index, arr) => {
            return (
                ruleIndexOut(curr, index, arr) ||
                ruleEqual(curr, index, arr) ||
                ruleOneMore(curr, index, arr)
            )
        },
        countUnique: (curr, index, arr) => {
            return (
                ruleIndexOut(curr, index, arr) || ruleOneMore(curr, index, arr)
            )
        },
        countUltraUnique: (curr, index, arr) => {
            return (
                ruleIndexOut(curr, index, arr) || ruleOneMore(curr, index, arr)
            )
        },
    }

    let hourArr = [sh[0], sh[1], sm[0], sm[1]]

    sortedHourArr = [...hourArr].sort()

    console.log(hourArr)

    log(`${sh}:${sm}`)

    if (
        sortedHourArr.every((curr, index, arr) => {
            return rules.count(curr, index, arr)
        })
    ) {
        count++
        log(`Count: ${h < 23 || m < 59} -> ${sh}:${sm} | ${sortedHourArr}`)
    }

    if (
        sortedHourArr.every((curr, index, arr) => {
            return rules.countUnique(curr, index, arr)
        })
    ) {
        countUnique++
        log(
            `Count Unique: ${
                h < 23 || m < 59
            } -> ${sh}:${sm} | ${sortedHourArr}`,
        )
    }

    if (
        hourArr.every((curr, index, arr) => {
            return rules.countUltraUnique(curr, index, arr)
        })
    ) {
        countUltraUnique++
        log(
            `Count Ultra Unique: ${
                h < 23 || m < 59
            } -> ${sh}:${sm} | ${hourArr}`,
        )
    }
}

// while (flag) {
//     if (h === 23 && m === 59) {
//         flag = false
//         break
//     }
//     if (m == 59) {
//         h++
//         m = 0
//     } else {
//         m++
//     }
//     if (h < 10) {
//         sh = "0" + h.toString()
//     } else {
//         sh = h.toString()
//     }
//     if (m < 10) {
//         sm = "0" + m.toString()
//     } else {
//         sm = m.toString()
//     }

//     s = [sh[0], sh[1], sm[0], sm[1]].sort().every((curr, index, arr) => {
//         if (curr == arr[index + 1] - 1 || curr == arr[index + 1] || index == 3)
//             return true
//         else return false
//     })

//     v = [sh[0], sh[1], sm[0], sm[1]].sort().every((curr, index, arr) => {
//         if (curr == arr[index + 1] - 1 || index == 3) return true
//         else return false
//     })

//     uv = [sh[0], sh[1], sm[0], sm[1]].every((curr, index, arr) => {
//         if (curr == arr[index + 1] - 1 || index == 3) return true
//         else return false
//     })

//     if (s) {
//         count++
//         // console.log(s, "=>", [sh[0], sh[1], sm[0], sm[1]])
//     } else {
//         // console.log([sh[0], sh[1], sm[0], sm[1]])
//     }

//     if (v) {
//         countUnique++
//         console.log(v, "-->", [sh[0], sh[1], sm[0], sm[1]])
//     } else {
//         // console.log([sh[0], sh[1], sm[0], sm[1]])
//     }

//     if (uv) {
//         countUltraUnique++
//         console.log(uv, "==>", [sh[0], sh[1], sm[0], sm[1]])
//     } else {
//         // console.log([sh[0], sh[1], sm[0], sm[1]])
//     }

//     // console.log(sh[0], sh[1], sm[0], sm[1])

//     // console.log(`${h < 23 || m < 59} -> ${sh}:${sm}`)
// }

console.log("Count: ", count)
console.log("Count Unique: ", countUnique)
console.log("Count Ultra Unique: ", countUltraUnique)
