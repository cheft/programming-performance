extern crate actix_web;

use actix_web::*;

fn index(_req: HttpRequest) -> &'static str {
    "Hello world!"
}

fn main() {
    HttpServer::new(
        || Application::new()
            .resource("/", |r| r.f(index)))
        .bind("0.0.0.0:8080").unwrap()
        .run();
}
