package com.example.rudra.dinoapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class MainActivity extends AppCompatActivity implements SensorEventListener {
TextView tv1,jumpCounter;
EditText et;
Button b1,b2,b3;
String ipv4;
Thread thread;
SensorManager sm;
double x,y,z,cac,lac,shake;
static int flag=0;
int status_connect=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        b1=findViewById(R.id.b1);
        et=findViewById(R.id.et);
        tv1=findViewById(R.id.tv1);
        jumpCounter=findViewById(R.id.jumpCounter);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ipv4=et.getText().toString();
                et.setText("Excercise and Play");
                sm=(SensorManager)getSystemService(SENSOR_SERVICE);
                sm.registerListener(MainActivity.this,sm.getDefaultSensor(Sensor.TYPE_ACCELEROMETER),SensorManager.SENSOR_DELAY_GAME);
                cac=SensorManager.GRAVITY_EARTH;
                lac=SensorManager.GRAVITY_EARTH;
                shake=0;
                tv1.setText("Connected");
                b1.setVisibility(View.INVISIBLE);
                jumpCounter.setText("0");
            }
        });
        et.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                et.setText("");
            }
        });
        b2=findViewById(R.id.b2);
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i=new Intent(MainActivity.this,activity_leaderb.class);
                startActivity(i);

            }
        });
        b3=findViewById(R.id.b3);
        b3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                b1.setVisibility(View.VISIBLE);
                MainActivity.this.finishAffinity();
            }
        });


    }

    @Override
    public void onSensorChanged(SensorEvent sensorEvent) {
        final Handler handler=new Handler();
        x=sensorEvent.values[0];
        y=sensorEvent.values[1];
        z=sensorEvent.values[2];
        // Log.d("servshk","x"+Double.toString(x));
        lac=cac;
        cac= Math.sqrt(x*x+y*y+z*z);
        double change=cac-lac;
        shake= shake + change;
        thread=new Thread(new Runnable(){
                public void run(){
                    try{
                        Socket sk=new Socket(ipv4,9002);
                        OutputStream out=sk.getOutputStream();
                        PrintWriter printW=new PrintWriter(out);
                        if(shake>15 && flag==0){
                        printW.print("Jump");
                        handler.post(new Runnable() {
                            @Override
                            public void run() {
                                jumpCounter.setText("Yipee");
                            }
                        });
                        flag=1;
                        }
                        else{
                            printW.print("Nope");
                            flag=0;
                            handler.post(new Runnable() {
                                @Override
                                public void run() {
                                    jumpCounter.setText("");
                                }
                            });
                        }
                        printW.flush();
                       // BufferedReader br=new BufferedReader(new InputStreamReader(sk.getInputStream()));
                        //final String res=br.readLine();
                       // Log.d("RICKY",res);
                        status_connect=1;
                    }catch(IOException e){
                        handler.post(new Runnable() {
                            @Override
                            public void run() {
                                jumpCounter.setText("Connection Error.\nTry Again!");
                                b1.setVisibility(View.VISIBLE);
                                et.setText("Enter Valid IP Again");
                            }
                        });
                        StringWriter errors = new StringWriter();
                        e.printStackTrace(new PrintWriter(errors));
                        Log.d("RICKY",errors.toString());
                    }
                }
            });
            thread.start();
        }


    @Override
    public void onAccuracyChanged(Sensor sensor, int i) {

    }
}
