  const http = require('http');
const fs = require('fs');
const path = require('path');

// 设置静态文件根目录
const staticRoot = path.resolve(__dirname, 'public');

path.isDir = (filePath) => {
    return fs.lstatSync(filePath).isDirectory();
}

// 删除目录
function deleteDirectory(directory) {
    if (fs.existsSync(directory)) {
        fs.readdirSync(directory).forEach((file) => {
            const filePath = path.join(directory, file);
            if (fs.lstatSync(filePath).isDirectory()) {
                deleteDirectory(filePath); // 递归删除子目录
            } else {
                fs.unlinkSync(filePath); // 删除文件
            }
        });
        fs.rmdirSync(directory); // 删除目录
        console.log(`Directory ${directory} deleted successfully`);
    } else {
        console.log(`Directory ${directory} does not exist`);
    }
}

// 创建 HTTP 服务器
const server = http.createServer((req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    // 获取请求的文件路径
    const filePath = path.join(staticRoot, req.url);
    if (path.normalize(decodeURI(req.url)) !== decodeURI(req.url)) {
        res.statusCode = 403;
        res.end();
        return;
    }

    try {
        if(req.method === 'GET') {
            if (path.isDir(filePath)) {
                res.writeHead(404);
                res.end(filePath + ' Is A Directory!');
            } else {
                // 判断请求的文件是否存在
                fs.access(filePath, fs.constants.F_OK, (err) => {
                    if (err) {
                        // 如果文件不存在，返回 404 Not Found
                        res.writeHead(404);
                        res.end(filePath + ' Not Found!');
                    } else {
                        // 根据文件扩展名设置响应头
                        const extname = path.extname(filePath);
                        if (extname === '.json') {
                            res.setHeader('Content-Type', 'application/json; charset=utf-8');
                        }
                        else if (extname === '.mp4') {
                            res.setHeader('Content-Type', 'video/mp4');
                        }
                        // 如果文件存在，读取文件并返回
                        fs.createReadStream(filePath).pipe(res);
                    }
                });
            }
        }
        else if (req.method === 'POST') {
            // 创建文件路径filePath对应的文件, 如果目录不存在，创建目录
            const dir = path.dirname(filePath);
            if (!fs.existsSync(dir)) {
                fs.mkdirSync(dir, {recursive: true});
            }
            const writeStream = fs.createWriteStream
            (filePath, {flags: 'w', encoding: 'utf-8'});
            // 获取请求的数据并写入文件
            req.pipe(writeStream);

        }
        else if (req.method === 'DELETE') {
            if(path.isDir(filePath)){
                // 处理目录删除
                deleteDirectory(filePath);
                res.writeHead(200);
                res.end('Directory deleted successfully');
            }
            else{
                // 处理文件删除
                fs.unlink(filePath, (err) => {
                    if (err) {
                        res.writeHead(500);
                        res.end('Internal Server Error');
                        return;
                    }
                    res.writeHead(200);
                    res.end('File deleted successfully');
                });
            }
        }
    }
    catch (err) {
        res.writeHead(500);
        res.end('Internal Server Error: ' + err);
    }


});

// 监听端口
const port = 3000;
server.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
