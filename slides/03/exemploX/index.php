<?php

# exemplo que mostra a importância do tipo de conteúdo.

header("Content-type: image/png");

$filename = getcwd().DIRECTORY_SEPARATOR."Imagem1.png";
echo file_get_contents($filename);

?>