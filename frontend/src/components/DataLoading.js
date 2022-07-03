import React from 'react';

function DataLoading(Component) {
    return function LoadingComponent({ isLoading, ...props}) {
        if (!isLoading) return <Component {...props} />;
        return (
            <p style={{ fontSize:'25px '}}>
                Waiting for data to load!...
            </p>
        )
    }
}

export default DataLoading;