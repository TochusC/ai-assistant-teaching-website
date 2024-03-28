export const particleOption = {
    fpsLimit: 120,
    interactivity: {
        events: {
            onClick: {
                enable: true,
                mode: 'push'
            },
            onHover: {
                enable: true,
                mode: 'repulse'
            },
        },
        modes: {
            bubble: {
                distance: 400,
                duration: 2,
                opacity: 0.8,
                size: 40
            },
            push: {
                quantity: 2
            },
            repulse: {
                distance: 50,
                duration: 0.4
            }
        }
    },
    particles: {
        color: {
            value: '#8080ff'
        },
        move: {
            direction: 'down',
            enable: true,
            outModes: 'bounce',
            random: false,
            speed: 0.4,
            straight: false
        },
        number: {
            density: {
                enable: true,
            },
            value: 160
        },
        opacity: {
            value: 0.5
        },
        shape: {
            type: 'circle'
        },
        size: {
            value: { min: 2, max: 6 }
        }
    },
    detectRetina: true
}