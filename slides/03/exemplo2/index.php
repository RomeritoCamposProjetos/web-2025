<?php

$method = $_SERVER['REQUEST_METHOD'];
$path = getcwd();
if ($method == 'POST') {
    ($_FILES['userfile']['name']);
    $name = $path.DIRECTORY_SEPARATOR.basename($_FILES['userfile']['name']);
    move_uploaded_file($_FILES['userfile']['tmp_name'], $name);
    exit;
    
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <form action="/" method="POST" enctype="multipart/form-data">
        <input type="file" placeholder="filename" name="userfile">
        <button>Enviar</button>
    </form>

</body>
</html>