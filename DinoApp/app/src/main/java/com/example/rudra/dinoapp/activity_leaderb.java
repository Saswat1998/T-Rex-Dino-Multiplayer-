package com.example.rudra.dinoapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class activity_leaderb extends AppCompatActivity {
TextView tv1,tv2;
Button b1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_leaderb);
        tv1=findViewById(R.id.textView5);
        tv2=findViewById(R.id.textView6);
        b1=findViewById(R.id.button);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(activity_leaderb.this, MainActivity.class);
                startActivity(i);
            }
        });
    }
}
