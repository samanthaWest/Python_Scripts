// Type Aliases

type Age = number

type Person2 = { 
    name: string,
    age: Age
}

// Dry Princaple Union & Intersection
type Cat = { name: string }
type Dog = { name: string, barks: boolean }
type CatOrDog = Cat | Dog
type CatAndDog = Cat & Dog

let misty : CatOrDog = {
    name: 'Bonkers',
    barks: true
}

// value | isnt one or the other it can be both at once

// Union Example

function trueOrNull(isTrue: boolean) {
    if (isTrue) {
        return 'True'
    }
    return null
}

// Returns string or null
// if a exists return string else b return number
function hmm(a: string, b: number) {
    return a || b
}

// Array Syntax
// Either T[] or Array <T>

let d = [1,'a']

d.map( _ => {
    if (typeof _ === 'number') {
        return _ * 3
    }
    return _.toUpperCase()
})

// Tuples Subtype of An Array

let sampleT: [string, string, string] = ['cat', 'dog', 'pig']

// Option tuple ele supported [number, number?[]]
// Tuple rest ele, they must be last and netered in correct oder

let friends: [string, ...string[]] = ['sara','tali',' jake']

// Enums

enum Lang {
    English,
    Spanish
}

console.log(Lang.English)

