package com.example.loginpage;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class HomeActivity extends AppCompatActivity {

    EditText emailEditText, passwordEditText;
    Button loginButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        // Initialize UI elements
        emailEditText = findViewById(R.id.emailEditText);
        passwordEditText = findViewById(R.id.passwordEditText);
        loginButton = findViewById(R.id.loginButton);

        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email = emailEditText.getText().toString().trim();
                String password = passwordEditText.getText().toString().trim();

                // Check login credentials (Simple example)
                if (email.equals("admin@example.com") && password.equals("123456")) {
                    Toast.makeText(HomeActivity.this, "Login Successful!", Toast.LENGTH_SHORT).show();
                    // Redirect to another activity (if needed)
                    // startActivity(new Intent(HomeActivity.this, DashboardActivity.class));
                } else {
                    Toast.makeText(HomeActivity.this, "Invalid email or password!", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
