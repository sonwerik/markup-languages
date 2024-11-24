function countLetter(frase, lletra) {
    let count = 0;
    for (let i = 0; i < frase.length; i++) {
        if (frase[i] === lletra) count++;
    }
    return count;
}
console.log(countLetter("institut", 't'));
