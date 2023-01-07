const button = document.getElementById("click-button");
const countSpan = document.getElementById('clicked-times')
// console.log('button')

let count = 0

// вариант с переопределением button.onclick
// button.onclick = function () {
//     console.log("here clicked too")
// }

// вариант без переопределения и с двойныйм выводом
function processButtonClick() {
    // console.log("here clicked too")
    count += 1
    updateValueOnPage()
}

function updateValueOnPage() {
    countSpan.innerText = count.toString()

}

button.addEventListener('click', processButtonClick)