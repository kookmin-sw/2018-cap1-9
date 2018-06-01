
<?
$db_host ="localhost";
$db_user = "root";
$db_password ="1234";
$db_name = "VT";
$conn = mysqli_connect($db_host,$db_user,$db_password,$db_name);

if(!$conn){
  die("connetction failed:" . mysqli_connect_error());
  }

  $list = addslashes($_GET["list"]);
  $No = addslashes($_GET["No"]);

  $query = "SELECT No FROM Clothes_Info where Picture_Addr = $list " ;
  $res =  mysqli_query($conn,$query);
  $row = $res -> fetch_array();
  $c_No = $row[0];

  mysqli_close($conn);

  ?>
  <html>
   <head>
      <script type="text/javascript">
        location.href='select_clothe.php?No=<? echo $c_No;?>&Picture_Addr=<? echo $list ;?>';
      </script>
   </head>

  </html>
