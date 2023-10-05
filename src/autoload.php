<?php

/**
 * @param string $dir
 * @param string $class
 * @return string|null
 */
function get_class_file_path(string $dir, string $class): ?string
{
    if (is_dir($dir)) {
        $resource = opendir($dir);
        while ($file = readdir($resource)) {
            if ($file != '.' && $file != '..') {
                if (is_file("$dir/$file") && $file == "$class.php") {
                    closedir($resource);
                    return "$dir/$file";
                } else {
                    $path = get_class_file_path($dir . DIRECTORY_SEPARATOR . $file, $class);
                    if (!is_null($path)) return $path;
                }
            }
        }
        closedir($resource);
    }
    return null;
}

spl_autoload_register(function ($class) {
    $path = get_class_file_path(__DIR__, $class);
    if (!is_null($path)) {
        require_once $path;
    }
});