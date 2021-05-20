var RandomOrg = require('random-org'); //chama o random.org

var random = new RandomOrg({ apiKey: '062cf2cc-24fa-42fb-a923-c7241d6bac13' }); //valida a chave
random.generateIntegers({ min: 1, max: 60, n: 6, replacement: Boolean }) //estabelece os limites e repetições
    .then(function (result) {
        console.log(result.random.data); //gera os números
    });