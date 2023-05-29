import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppServiceCatch } from './app.service';

@Module({
  imports: [],
  controllers: [AppController],
  providers: [AppServiceCatch],
})
export class AppModule {}
