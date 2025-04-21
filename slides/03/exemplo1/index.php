<?php
$method = $_SERVER['REQUEST_METHOD'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <?php
        if ($method == 'POST') {
            $valor = $_POST['valor'];
            echo "<script>";
            echo "alert('$valor')";
            echo "</script>";            
        }
    ?>

</head>
<body>
    <form action="/" method="POST" enctype="application/x-www-form-urlencoded">
        <input type="text" placeholder="Texto" name="valor">
        <button>Enviar</button>
    </form>    
</body>
</html>