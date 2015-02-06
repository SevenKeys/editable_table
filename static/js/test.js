var sqr = '[';
var sql = ']';
var fr = '{';
var fl = '}';
var rr = '(';
var rl = ')';
var stroka = '[]][[(){}]])';

function check(stroka){
	for (var i in stroka){
		if (stroka[i] === sqr){
			count_sqr +=1
		}else if(stroka[i] === sql){
			count_sql +=1;
			if (stroka[i-1] !== sqr){
				alert('Order of brackets is disturb');
			}
		}else if(stroka[i] === fr){
			count_fr +=1;

		}else if(stroka[i] === fl){
			count_fl +=1;
			if (stroka[i-1] !== fr){
				alert('Order of brackets is disturb');
			}
		}else if(stroka[i] === rr){
			count_rr +=1;
		}else if(stroka[i] === rr){
			count_rl +=1;
			if (stroka[i-1] !== rr){
				alert('Order of brackets is disturb');
			}
		}
		if count_sqr !== count_sql{
			alert('squre brackets do not match')
		}else if count_fr !== count_fl{
			alert('figure brackets do not match')
		}else if count_rr !== count_rl{
			alert('round brackets do not match')
		} 
	}
}

