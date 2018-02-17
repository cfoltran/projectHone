import React from 'react';

const steps=[
    {
        id: '1',
        message: 'Vous cherchez des informations ?',
        trigger: '2',
    },
    {
        id: '2',
        options: [
            { value: 1, label: 'Le concept ?', trigger: '4' },
            { value: 2, label: 'Notre Twitter', trigger: '3' },
        ],
    },
    {
        // todo fix error previous step
        id: '3',
        component: (
            <div>
                <a target="_blank" rel="noopener noreferrer" href="https://twitter.com/twot_bot">Cliquez ici pour aller sur Twitter.</a>
            </div>
        ),
        asMessage: true,
        trigger: '9'
    },
    {
        id: '4',
        message: 'Le concept est ...',
        trigger: '9'
    },
    {
        id: '9',
        message: 'D\'autres informations ?',
        trigger: '2'
    },
];

export default steps;