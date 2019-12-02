#include <FastLED.h>
#define LED_PIN 23
#define NUM_LEDS 60
#define BRIGHTNESS 96
#define LED_TYPE WS2812B
#define COLOR_ORDER GRB
CRGB leds[NUM_LEDS];

#define UPDATES_PER_SECOND 100

// set pin numbers to names for easy reference
const int switch_1 = 12;
const int switch_2 = 11;
const int switch_3 = 10;
const int switch_4 = 9;
const int switch_5 = 8;
const int switch_6 = 7;
const int switch_7 = 6;
const int switch_8 = 5;
const int button_1 = 48;
const int button_2 = 44;
const int button_3 = 40;
const int button_4 = 34;
const int button_5 = 36;
const int button_6 = 41;
const int button_7 = 37;
const int button_8 = 33;
const int green_led = 24;
const int yellow_led = 26;
const int red_led = 28;
const int white_led = 53;
const int blue_led = 49;
const int buzzer_pin = 35;

// variables for game system
int game_speed = 0;
int game_mode = 0;


void setup() {
    // setup code for LED strip
    delay(  3000  ); // 3 second safety delay
    FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
    FastLED.setBrightness(  BRIGHTNESS  );

    // initialize pin modes (input or output)
    pinMode(switch_1, INPUT);
    pinMode(switch_2, INPUT);
    pinMode(switch_3, INPUT);
    pinMode(switch_4, INPUT);
    pinMode(switch_5, INPUT);
    pinMode(switch_6, INPUT);
    pinMode(switch_7, INPUT);
    pinMode(switch_8, INPUT);
    pinMode(button_1, INPUT);
    pinMode(button_2, INPUT);
    pinMode(button_3, INPUT);
    pinMode(button_4, INPUT);
    pinMode(button_5, INPUT);
    pinMode(button_6, INPUT);
    pinMode(button_7, INPUT);
    pinMode(button_8, INPUT);
    pinMode(green_led, OUTPUT);
    pinMode(yellow_led, OUTPUT);
    pinMode(red_led, OUTPUT);
    pinMode(white_led, OUTPUT);
    pinMode(blue_led, OUTPUT);


     // read switches
    if (digitalRead(switch_1) == HIGH){
        game_speed = 5000;
    }
    else if (digitalRead(switch_2) == HIGH){
        game_speed = 10000;
    }
    else if (digitalRead(switch_3) == HIGH){
        game_speed = 15000;
    }
    else if (digitalRead(switch_4) == HIGH){
        game_speed = 20000;
    }
    else if (digitalRead(switch_5) == HIGH){
        game_speed = 30000;
    }
    else if (digitalRead(switch_6) == HIGH){
        game_speed = 60000;
    }
    if (digitalRead(switch_7) == HIGH){
        game_mode = 1;
    }
    else if (digitalRead(switch_8) == HIGH){
        game_mode = 2;
    }

}

// create a function with parameters as
// c = color
void myledstrip(int c){
    switch (c){
      case 1:
    for (int i = 0; i < NUM_LEDS; i++){
    leds[i].setRGB(100, 100, 100);
    }
    FastLED.show();
      break;

      case 2:
    for (int i = 0; i < NUM_LEDS; i++){
    leds[i] = CRGB::Red;
    }
    FastLED.show();
      break;

      case 3:
    for (int i = 0; i < NUM_LEDS; i++){
    leds[i] = CRGB::Green;
    }
    FastLED.show();
      break;

      case 4:
    for (int i = 0; i < NUM_LEDS; i++){
    leds[i] = CRGB::Blue;
    }
    FastLED.show();
      break;

    default:
    for (int i = 0; i < NUM_LEDS; i++){
    leds[i] = CRGB::Black;
    }
    FastLED.show();
    break;
    }
}


int remaining_player_1 = 0;
int remaining_player_2 = 0;
int remaining_player_1_led = 0;
int remaining_player_2_led = 0;
int last_player = 0;
int last_player_led = 0;
int response_button_check = 0;
int strip1 = 0;
int strip2 = 0;
int strip3 = 0;
bool dont_blink_strip = false;
int blink_strip_delay = 100;
int strip_blink_times = 4;




void loop() {
    digitalWrite(green_led, LOW);
    digitalWrite(yellow_led, LOW);
    digitalWrite(red_led, LOW);
    myledstrip(0);
    // check for game mode
    if (game_mode == 1){ // todo game start
        // start game
        digitalWrite(blue_led, HIGH);
        bool wait = true;
        while (wait == true){
            if (digitalRead(button_4) == HIGH) {
                wait = false;
            }

            if (digitalRead(button_6) == HIGH) {
                for (int i = 0; i <= 10; i++){
                    leds[i] = CRGB::White;
                }
                for (int i = 20; i <= 30; i++){
                    leds[i] = CRGB::White;
                }
                for (int i = 40; i <= 50; i++){
                    leds[i] = CRGB::White;
                }
                    FastLED.show();
                delay(50);
                myledstrip(0);
                for (int i = 10; i <= 20; i++){
                    leds[i] = CRGB::White;
                }
                for (int i = 30; i <= 40; i++){
                    leds[i] = CRGB::White;
                }
                for (int i = 50; i <= 60; i++){
                    leds[i] = CRGB::White;
                }
                FastLED.show();
                delay(50);
                myledstrip(0);
            }

            if (digitalRead(button_7) == HIGH) {
//                 int x = 60;
//                 for (int y = 0; y <= x, y++){
//                     leds[y] = CRGB::Tan;
//                     FastLED.show();
//                 }
//                 delay(2000);
//                 x = 55;
                myledstrip(1);
                for (int z = 0; z <= 15; z++){
                    for (int x = 60; x >= 0; x = x - 2){
                    int y = x + 1;
                    leds[x] = CRGB::Black;
                    leds[y] = CRGB::Black;
                    FastLED.show();
                    delay(1000);
                    }
                }
            }
        }
            // indicate that the buttons can now be pressed
            delay(300);
            digitalWrite(white_led, HIGH);
            myledstrip(1);
        int button_number = 0;
        for (int i = 500; i >= 0; i--){ // todo white strip
            if (digitalRead(button_1) == HIGH){
                button_number = 1;
                digitalWrite(green_led, HIGH);
                myledstrip(3);
                remaining_player_1 = button_2;
                remaining_player_1_led = yellow_led;
                remaining_player_2 = button_3;
                remaining_player_2_led = red_led;
                strip1 = 4;
                strip2 = 2;
                strip3 = 3;
            }
            else if (digitalRead(button_2) == HIGH){
                button_number = 2;
                digitalWrite(yellow_led, HIGH);
                myledstrip(4);
                remaining_player_1 = button_1;
                remaining_player_1_led = green_led;
                remaining_player_2 = button_3;
                remaining_player_2_led = red_led;
                strip1 = 3;
                strip2 = 2;
                strip3 = 4;
            }
            else if (digitalRead(button_3) == HIGH){
                button_number = 3;
                digitalWrite(red_led, HIGH);
                myledstrip(2);
                remaining_player_1 = button_1;
                remaining_player_1_led = green_led;
                remaining_player_2 = button_2;
                remaining_player_2_led = yellow_led;
                strip1 = 3;
                strip2 = 4;
                strip3 = 2;
            }
            if (button_number > 0) {
                break;
            }
            if (digitalRead(button_5) == HIGH){
                dont_blink_strip = true;
                break;
            }
            delay(10);
        } digitalWrite(white_led, LOW);
        delay(300);
        //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        for (int i = game_speed / 10; i >= 0; i--){ // chance to answer // todo color strip
            if (button_number == 0){
                dont_blink_strip = true;
                break;
            }

            // if answer is correct
            if (digitalRead(button_5) == HIGH){
                dont_blink_strip = true;
                break;
            }

            if (digitalRead(button_4) == HIGH){ // WRONG answer
                // if the first player to buzz in got the answer wrong
                break;
                dont_blink_strip = false;
            }
            dont_blink_strip = false;
        delay(10);
        }// response check



        if (dont_blink_strip == false){
            myledstrip(0);
            for (int x = 0; x <= strip_blink_times; x++){
                delay(blink_strip_delay);
                myledstrip(strip3);
                delay(blink_strip_delay);
                myledstrip(0);
            }
            delay(blink_strip_delay);
        }
        dont_blink_strip = true;



        if (button_number > 0){
        // give the other players a chance
            digitalWrite(white_led, HIGH);
            digitalWrite(green_led, LOW);
            digitalWrite(yellow_led, LOW);
            digitalWrite(red_led, LOW);
            myledstrip(1);
        }

        // first wrong answer white strip
        if (button_number > 0){
            button_number = 0;
            for (int x = 500; x >= 0; x--){ // todo white strip
                if (digitalRead(remaining_player_1) == HIGH){
                    button_number = 1;
                    digitalWrite(remaining_player_1_led, HIGH);
                    myledstrip(strip1);
                    strip3 = strip1;
                }
                else if (digitalRead(remaining_player_2) == HIGH){
                    button_number = 2;
                    digitalWrite(remaining_player_2_led, HIGH);
                    myledstrip(strip2);
                    strip3 = strip2;
                }
                if (button_number > 0) {
                    dont_blink_strip = false;
                    break;
                }
                if (digitalRead(button_5) == HIGH){
                    dont_blink_strip = true;
                    break;
                }
                delay(10);
                dont_blink_strip = false;
                } digitalWrite(white_led, LOW);


            // color strip
            for (int x = game_speed / 10; x >= 0; x--){ // todo color strip
                if (digitalRead(button_5) == HIGH){
                    dont_blink_strip = true;
                    break;
                }

                if (digitalRead(button_4) == HIGH){
                    // if the second player to buzz in got the answer wrong
                    dont_blink_strip = false;
                    break;
                }
                delay(10);
            }

            if (dont_blink_strip == false){
                myledstrip(0);
                for (int x = 0; x <= strip_blink_times; x++){
                    delay(blink_strip_delay);
                    myledstrip(strip3);
                    delay(blink_strip_delay);
                    myledstrip(0);
                }
                delay(blink_strip_delay);
            }
            dont_blink_strip = true;
        }

    delay(10);
    }











    if (game_mode == 2){
        while (true){
        int delay_number = 3;
            // christmas test code
           if (digitalRead(switch_2) == HIGH){
               delay_number = 100;
           }
           if (digitalRead(switch_3) == HIGH){
               delay_number = 50;
           }
           if (digitalRead(switch_4) == HIGH){
               delay_number = 10;
           }
           if (digitalRead(switch_5) == HIGH){
               delay_number = 3;
           }
           for (int i = 0; i < 60; i++){
           leds[i] = CRGB::Red;
           FastLED.show();
           FastLED.delay(delay_number);
           }

           for (int i = 0; i < 60; i++){
               leds[i] = CRGB::Green;
               FastLED.show();
               FastLED.delay(delay_number);
           }
        }
    }
}