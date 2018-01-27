<!-- curl  -i POST  --data "fname=chandu&lname=muthyala"  http://qav2.cs.odu.edu/chandu/WebSciences/A1/problem1.php --> 
<!DOCTYPE html>
<html>
<body>
<?php
	 echo "<br />";
	 echo "<br />";
     echo "<b>fname Posted: </b>" . $_POST['fname'] . "<br />";
     echo "<b>lname Posted: </b>" . $_POST['lname'] . "<br />";
?>

</body>
</html>