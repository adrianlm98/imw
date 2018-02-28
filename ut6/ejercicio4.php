
<html>
    <body>
        <form action="ejercicio4.php" method="post">
            <label for="fila">filas:</label>
                <input type="text" name="fila"/><br>

            <label for="columna">columnas:</label>
                <input type="text" name="columna"/><br>

            <input type="submit" value="Enviar"/>
        </form>
        <table border="1">
        <?php
            if (isset($_POST["fila"]) and isset($_POST["columna"])) {
                $fila = (float)$_POST["fila"];
                $columna = (float)$_POST["columna"];
                $colum = 1;
                $fil = 1;
                if ($fila >= 1 and $columna >= 1) {
                    echo("<p>Tabla:</p>");
                    while ($fil<=$fila) {
                        $fil++;
                        echo("<tr>");
                        while ($colum<=$columna) {
                            $colum++;
                            echo("<td>Nuevo</td>");
                        }
                        $colum = 1;
                        echo("</tr>");
                    }
                }
                else{
                    echo("Error");
                }
            }
        ?>
        </table>
    </body>
</html>