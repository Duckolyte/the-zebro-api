const test0 = {
    "id": "1",
    "parcSection":
        {},
    "date":
        {},
    "observationActions":
        [
            {
                "id": "22"
            },
            {
                "id": "33"
                "name": "Guido"
            }
        ],
    "species": "Giraffe"
}


const test1 = {
    "id": "1",
    "parcSection":
        {},
    "date":
        {},
    "observationActions":
        [
            {
                "id": "22"
            },
            {
                "id": "33"
                "name": "Guido"
            }
        ],
    "species": "Krokodil"
}

const test2 = {
    "id": "1",
    "parcSection":
        {},
    "date":
        {},
    "observationActions":
        [
            {
                "id": "22",
                "name": "Peter"
            },
            {
                "id": "33",
                "name": "Guido"
            }
        ],
    "species": "Giraffe"
}


const arrayTest = [test0, test1, test2];

arrayTest.filter(animal => animal.species == "Giraffe").filter(animal => animal.spacies == "Giraffe" && animal.observationActions.filter(action => action.name == "Peter")) // [test0, test2];

arrayTest.filter(function (x) {
    return x.species == "Giraffe";
})
