Install your dependencies

```
composer install
```

Please check [https://getcomposer.org/](https://getcomposer.org/) for more information. 

After that add your twitter tokens to your `config.php` file. Firstly, copy 
`.dist` file.

```
cp config.py.dist config.py
```

Finally, run your app

```
php stream.php keyword1 keyword2
```