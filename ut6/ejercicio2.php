<html>
    <body>
        <?php
            $salario = (float)$_POST["salario"];
            $nombre = $_POST["nombre"];
            $edad = (int)$_POST["edad"];
            $apellidos = $_POST["apellidos"];

            if ($salario <= 2000 and $salario >= 1000) {
                if ($edad > 45){
                    $salario = $salario + ($salario * 3)/100;
                }
                else{
                    $salario = $salario + ($salario * 10)/100;
                }
            }
            elseif ($salario < 1000){
                if ($edad < 30){
                    $salario = 1100;
                }
                elseif ($edad >= 30 and $edad <= 45){
                    $salario = $salario + ($salario * 3)/100;
                }
                else{
                    $salario = $salario + ($salario * 15)/100;
                }
            }
        echo("<h1>Nuevo salario:</h1><p>Nombre: $nombre<p>");
        echo("<p>Edad: $edad<p>");
        echo("<p>Salario: $salario<p>");
        echo("<p>Apellidos: $apellidos<p>");


        ?>
    </body>
</html>