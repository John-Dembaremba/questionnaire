# Create/Update/Retrieve/List----> Questionnaire with questions

```
Request http://localhost:8000/api/v1/questionnaire/ or http://localhost:8000/api/v1/questionnaire/{id}

Payload: {
    "name": "Member's Questionnaire",
    "for_members": true,
    "questions": [
        {"question": "Neurological Disorder: Migrane, Stroke, Epilepsy ?"},
        {"question": "Any mental disorder?"},
        {"question": "Are you pregnat? If so what is the expexted date of delivery"}
        
    ]
}

Response: {
    "id": 81,
    "name": "Member's Questionnaire",
    "for_members": true,
    "questions": [
        {
            "id": 102,
            "question": "Neurological Disorder: Migrane, Stroke, Epilepsy ?",
            "created_date": "2022-04-08T11:30:31.208118Z",
            "updated_date": "2022-04-08T11:30:31.208153Z"
        },
        {
            "id": 103,
            "question": "Any mental disorder?",
            "created_date": "2022-04-08T11:30:31.236875Z",
            "updated_date": "2022-04-08T11:30:31.236911Z"
        },
        {
            "id": 104,
            "question": "Are you pregnat? If so what is the expexted date of delivery",
            "created_date": "2022-04-08T11:30:31.283323Z",
            "updated_date": "2022-04-08T11:30:31.283401Z"
        }
    ]
}

```

# Create/Update/Retrieve/List----> UserResponse(supply info for a questionnaire)
```
http://localhost:8000/api/v1/questionnaire/user-answers/ or http://localhost:8000/api/v1/questionnaire/user-answers/{id}

Payload: {
    "user": "56f6ed19-deb6-432e-b598-e515702833b1",
    "questionnaire": 81,
    "response": [
        {
            "question": 102,
            "answer": true,
            "full_details": "since childhood"
        },
        {
            "question": 103,
            "answer": false,
            "full_details": null
        },
        {
            "question": 104,
            "answer": true,
            "full_details": "since highschool"
        }

    ]
}

Response: {
    "id": 25,
    "user": "56f6ed19-deb6-432e-b598-e515702833b1",
    "questionnaire": 81,
    "response": [
        {
            "id": 24,
            "question": 104,
            "answer": true,
            "full_details": "since highschool"
        },
        {
            "id": 22,
            "question": 102,
            "answer": true,
            "full_details": "since childhood"
        },
        {
            "id": 23,
            "question": 103,
            "answer": false,
            "full_details": null
        }
    ],
    "other_conditions": null
}

Response if user is not a member: {
    "message": "Sorry, the questionnaire is for members only"
}

//If answer is true but no full details provided

Payload: {
    "user": "56f6ed19-deb6-432e-b598-e515702833b1",
    "questionnaire": 81,
    "response": [
        {
            "question": 102,
            "answer": true,
            "full_details": "since childhood"
        },
        {
            "question": 103,
            "answer": true,
            "full_details": null
        },
        {
            "question": 104,
            "answer": true,
            "full_details": "since highschool"
        }

    ]
}

Response:{
    "question": "Any mental disorder?",
    "answer": true,
    "message": "Please provide full details for your answer."
}

```