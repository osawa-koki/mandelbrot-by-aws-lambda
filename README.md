# mandelbrot-by-aws-lambda

ðµðµðµ AWS Lambdaã§ãã³ãã«ãã­éåãæç»ãããµã³ãã«ã§ãã  

![ææç©](./docs/img/fruit.png)  
![ææç©](./docs/img/fruit.gif)  

## ç°å¢æå ±

| Name | Version |
| --- | --- |
| AWS CLI | 2.9.17 |
| AWS SAM CLI | 1.73.0 |
| Docker | 20.10.17 |

## ã¤ã­ã¤ã­æå ±

### AWS CLIã®ã¤ã³ã¹ãã¼ã«

[å¬å¼ãã¼ã¸](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2.html)ã®èª¬æã«æ²¿ã£ã¦ãã¤ã³ã¹ãã¼ã«ãã¾ãã  

### Dockerã®ã¤ã³ã¹ãã¼ã«

[å¬å¼ãã¼ã¸](https://docs.docker.com/get-docker/)ã®èª¬æã«æ²¿ã£ã¦ãã¤ã³ã¹ãã¼ã«ãã¾ãã  

### AWS SAM CLI ã®ã¤ã³ã¹ãã¼ã«

[å¬å¼ãã¼ã¸](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/install-sam-cli.html)ã®èª¬æã«æ²¿ã£ã¦ãã¤ã³ã¹ãã¼ã«ãã¾ãã  
AWS SAM CLIã¨ã¯ãServerless Application Model ã®ç¥ç§°ã§AWS Lambdaã®ã­ã¼ã«ã«å®è¡ç°å¢ãæä¾ãããã¼ã«ã§ãã  

---

åæã¨ãã¦ã`AWS CLI`ãã¤ã³ã¹ãã¼ã«ããã¦ããå¿è¦ãããã¾ãã  
`AWS CLI`ã®ã¤ã³ã¹ãã¼ã«æ¹æ³ã¯ã[å¬å¼ãã¼ã¸](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2.html)ãåç§ãã¦ãã ããã  

### ã©ã ããã­ã¸ã§ã¯ãã®ä½æ

ä»¥ä¸ã®ã³ãã³ãã§ããã­ã¸ã§ã¯ããä½æãã¾ãã  

```shell
sam init
```

å¯¾è©±å½¢å¼ã§ããã­ã¸ã§ã¯ãã®è¨­å®ãè¡ãã¾ãã  

```shell
You can preselect a particular runtime or package type when using the `sam init` experience.
Call `sam init --help` to learn more.

Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
        1 - Hello World Example
        2 - Multi-step workflow
        3 - Serverless API
        4 - Scheduled task
        5 - Standalone function
        6 - Data processing
        7 - Infrastructure event management
        8 - Serverless Connector Hello World Example
        9 - Multi-step workflow with Connectors
        10 - Lambda EFS example
        11 - Machine Learning
Template: 1

Use the most popular runtime and package type? (Python and zip) [y/N]: y

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: N

Would you like to enable monitoring using CloudWatch Application Insights?
For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: N

Project name [sam-app]: mandelbrot-by-aws-lambda

Cloning from https://github.com/aws/aws-sam-cli-app-templates (process may take a moment)

    -----------------------
    Generating application:
    -----------------------
    Name: mandelbrot-by-aws-lambda
    Runtime: python3.9
    Architectures: x86_64
    Dependency Manager: pip
    Application Template: hello-world
    Output Directory: .

    Next steps can be found in the README file at ./mandelbrot-by-aws-lambda/README.md


Commands you can use next
=========================
[*] Create pipeline: cd mandelbrot-by-aws-lambda && sam pipeline init --bootstrap
[*] Validate SAM template: cd mandelbrot-by-aws-lambda && sam validate
[*] Test Function in the Cloud: cd mandelbrot-by-aws-lambda && sam sync --stack-name {stack-name} --watch
```

### ã­ã¼ã«ã«ã§ã®å®è¡

ä»¥ä¸ã®ã³ãã³ãã§ãã­ã¼ã«ã«ã§å®è¡ã§ãã¾ãã  

```shell
sam build --use-container
sam local start-api
```

ãªã¯ã¨ã¹ãã®éä¿¡ãã³ãã³ãã§åæã«è¡ãå ´åã¯ãä»¥ä¸ã®ã³ãã³ããå®è¡ãã¾ãã  

```shell
sam local invoke
```

### ããã­ã¤

ä»¥ä¸ã®ã³ãã³ãã§ãããã­ã¤ã§ãã¾ãã  

```shell
sam build --use-container
sam deploy [--guided]
```

ååããã­ã¤å¾ã¯ãªã½ã¼ã¹ãã¼ã¹ã®ããªã·ã¼ã§ãããªãã¯ã¢ã¯ã»ã¹ãè¨±å¯ããå¿è¦ãããã¾ãã  
ããã¯ãã»ã­ã¥ãªãã£ä¸ã®çç±ãããããã©ã«ãã§ã¯è¨±å¯ããã¦ããããAWSã³ã³ã½ã¼ã«ããè¨±å¯ãããã¨ãã§ãã¾ããã  
â»[å¬å¼ãµã¤ã](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/urls-auth.html)ããã  
ãã®ç¶æã§ãããã­ã¤ããAPIã®URLã«ã¢ã¯ã»ã¹ããã¨ã`403 Forbidden`ãè¿ã£ã¦ãã¾ãã  

é¢æ°ãé¸æãããè¨­å® - é¢æ°URLãã¸é²ã¿ãç·¨éã¿ããã¯ãªãã¯ããJSONã³ã¼ãã®`principal`ã`*`ã«å¤æ´ãã¾ãã  
ããã§ä¿å­ããã¨ã¢ã¯ã»ã¹ã§ãã¾ãã  

![ãããªãã¯ã¢ã¯ã»ã¹ã®è¨±å¯](./docs/img/allow-public-access.gif)  

### åé¤

ä»¥ä¸ã®ã³ãã³ãã§ãAWS SAMã§æ§ç¯ãããªã½ã¼ã¹ãåé¤ã§ãã¾ãã  

```shell
sam delete
```

## èªåç¨ã¡ã¢

### ã©ã ãã§æå­åä»¥å¤ãè¿ã

æ»ãå¤ã®è¾æ¸ãã¼ã¿ã®`isBase64Encoded`ã`True`ã«ãã`Body`ã«base64ã¨ã³ã³ã¼ããããã¤ããªãã¼ã¿ãå¥ããã  
ãã®ã¾ã¾è¿ããã¨ããã¨ãæå­åã¨ãã¦è§£æããã¦ã¨ã©ã¼ãçºçããã  

### é¢æ°ã®å¼æ°ã«æ³¨æ

APIã²ã¼ãã¦ã§ã¤ãä½¿ç¨ããå ´åã¨ãé¢æ°URLãç´æ¥å©ããå ´åã§ãå¼æ°ã®ãã¼ã¿åãç°ãªãç¹ã«æ³¨æããã  
