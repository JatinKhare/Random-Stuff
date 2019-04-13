<!DOCTYPE html>
<html>
<head>
	<title>Binary to Decimal converter</title>
</head>
<body>
<p>Enter the binary number below:</p>

<form method="post" action="bin2dec.php">
<input type="text" id="number" name = 'number' placeholder="Enter number here" maxlength="19">
<input type = "submit" placeholder="Submit">
</form>

<?php
	error_reporting(0);
	$length = strlen($_POST['number']);
	$flag = true;
	for ($i = 0;$i < $length;$i++){
		if (($_POST['number'][$i] == '1') || ($_POST['number'][$i] == '0')){
			$flag = true;
		}
		else{
			$flag = false;
		}
 	}
 	if ($flag == true){
		$var = (int)$_POST['number'];
		$length = strlen($_POST['number']);
		$sum = 0;
		for ($x = 0; $x < $length ; $x++){
			$r = $var%10;
			$var = intdiv($var,10);
			if ($r == 1){
				$sum = $sum + pow(2,$x);
			}
		}
		echo "\n The decimal equivalent of the binary number is\n";
		echo $sum;
	}
	else{
		echo "<script>alert('You can enter only 0 and 1!'); location.href='bin2dec.php';</script>";
	}	
?>

</body>
</html>