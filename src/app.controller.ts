import { Controller, Get, Post,Body, Headers, HttpException} from '@nestjs/common';
import { AppService } from './app.service';


@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Post("analyze")
  async analyze(@Headers() headers, @Body() message){

    const responseFromAnalyze = await this.appService.postAnalyze(headers, message);
    console.log("body dddd",responseFromAnalyze)
    if (responseFromAnalyze.responseStatus == 200){
      console.log("body",responseFromAnalyze.body)
      return responseFromAnalyze.body;
    }else{
      throw new HttpException(responseFromAnalyze.statusText, responseFromAnalyze.responseStatus);
    }

  }
}
