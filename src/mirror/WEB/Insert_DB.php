
<?
$db_host ="localhost";
$db_user = "root";
$db_password ="1234";
$db_name = "VT";
$conn = mysqli_connect($db_host,$db_user,$db_password,$db_name);

if(!$conn){
  die("connetction failed:" . mysqli_connect_error());
  }

$No = addslashes($_GET["No"]);

$sql = "UPDATE Clothes_Info SET IsUpdate ='1' WHERE No = $No";
if (mysqli_query($conn,$sql)){
  }
  else{ echo "Error: " .$sql . "<br>" . mysqli_error($conn);
  }

mysqli_close($conn);

?>
<html>
 <head>
    <script type="text/javascript">
       location.href='clothes_list.php';
    </script>
 </head>

</html>
