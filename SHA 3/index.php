<?php
require_once 'SHA3.php';

if (isset($_POST['hash'])) {
    $file = $_FILES['file']['tmp_name'];
    $h = file_get_contents($file);
    $code = bin2hex(SHA3::init(SHA3::SHA3_256)->absorb($h)->squeeze());
}

if (isset($_POST['cek'])) {
    $file = $_FILES['file']['tmp_name'];
    $h = file_get_contents($file);
    $t = $_POST['t'];

    if (hex2bin($t) === SHA3::init(SHA3::SHA3_256)->absorb($h)->squeeze()) {
        $code = 'File Sesuai!';
    } else {
        $code = 'File tidak sesuai atau sudah dimodifikasi!';
    }
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    <title>Checksum SHA3</title>
</head>

<body>
    <div class="container">
        <div class="row">
            <form action="javascript:void(0)" method="post" enctype="multipart/form-data">
                <div class="col-lg-12">
                    <div class="form-group">
                        <label class="custom-file">
                            <input type="file" name="file" class="form-control-file" aria-describedby="fileHelpId">
                            <span class="custom-file-control"></span>
                        </label>
                        <small id="fileHelpId" class="form-text text-muted">Upload File Disini</small>
                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="form-group">
                        <label for="hash">Hash</label>
                        <textarea class="form-control" name="t" rows="3"><?php echo @$code ?></textarea>
                    </div>
                </div>
                <div class="col-lg-12">
                    <button type="submit" name="hash" class="btn btn-primary">Hash</button>
                    <button type="submit" name="cek" class="btn btn-warning">Check</button>
                </div>
            </form>
        </div>
    </div>
</body>

</html>