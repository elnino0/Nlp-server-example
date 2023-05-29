import { Test, TestingModule } from '@nestjs/testing';
import { INestApplication } from '@nestjs/common';
import * as request from 'supertest';
import { AppModule } from './../src/app.module';

describe('AppController (e2e)', () => {
  let app: INestApplication;

  beforeEach(async () => {
    const moduleFixture: TestingModule = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = moduleFixture.createNestApplication();
    await app.init();
  });

  it('fail post ', () => {
    return request(app.getHttpServer())
      .post('/any')
      .send({"text":"1234"})
      .set('Content-Type', 'application/json')
      .set('Accept', 'application/json')
      .expect(404);
  });
});
