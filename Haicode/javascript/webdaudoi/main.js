
function passwwordMeter(password){
    var result 
    let strengthValuea = false
    let strengthValueb = {
        'caps': false,
        'special': false,
        'numbers': false,
        'small': false
    };

    if(password.length >= 8) {
        strengthValuea = true;
    }
    for(let index=0; index < password.length; index++) {
        let char = password.charCodeAt(index);
        if(!strengthValueb.caps && char >= 65 && char <= 90) {
            strengthValueb.caps = true;
        } else if(!strengthValueb.numbers && char >=48 && char <= 57){
          strengthValueb.numbers = true;
        } else if(!strengthValueb.small && char >=97 && char <= 122){
          strengthValueb.small = true;
        } else if(!strengthValueb.numbers && char >=48 && char <= 57){
          strengthValueb.numbers = true;
        } else if(!strengthValueb.special && (char >=33 && char <= 47) || (char >=58 && char <= 64)) {
          strengthValueb.special = true;
        }
    }
    var checkStrong = 0
    for(let cases in strengthValueb){
        if(strengthValueb[cases] === true  ){
            checkStrong++
        }
    }
    if(checkStrong !== 4 && strengthValuea === false ){
        return 'Weak'
    }
    else if (strengthValuea === true && checkStrong === 4 ){
        return 'Strong'
    }
    else if (strengthValuea === true || checkStrong === 4 ){
        return 'Good'
    }
}

console.log(passwwordMeter('aaa@ABe34'))